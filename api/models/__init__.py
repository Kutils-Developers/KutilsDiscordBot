from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple
from pathlib import Path
from datetime import datetime
from api.dataservices.google.sheets.utils import Cell
from api.dataservices.google.sheets import get_cells
from api.support import APIError
import api
import jsons
import logging


@dataclass
class TrackedSheet:
    # change the sheet, add a cellrange, get updates for its own sheet
    sheet_id: str
    cell_ranges: List[str]

    def get_updates(self):
        # cell - initialize itself & know the service it is, returns if its dead or not
        cells = get_cells(self.sheet_id, self.cell_ranges)
        return [c for c in cells if c.is_dead()]


@dataclass
class SheetWatcher:
    """Assumes that a SheetWatcher is uniquely defined by their name"""
    # change time it updates, get the next time it updates, return its name, get all updates for a specific sheet on a timely basis
    name: str
    tracked_sheet: Optional[TrackedSheet] = None
    utc_offset: Optional[int] = 72680

    def get_name(self) -> str:
        return self.name

    def set_name(self, newname: str):
        self.name = newname

    def set_tracked_sheet(self, ts: TrackedSheet):
        self.tracked_sheet = ts

    def get_tracked_sheet(self) -> TrackedSheet:
        return self.tracked_sheet

    def __eq__(self, other):
        if type(other) == type(self):
            return other.name == self.name
        return False

    def get_updates(self):
        if not self.tracked_sheet:
            raise APIError(f'job {self.name} does not have a TrackedSheet')
        return self.tracked_sheet.get_updates()


@dataclass
class Instance:
    """Bot Instance API Object. Assumes that Instances are uniquely defined by guild_id"""
    # TODO use .get_jobs instead of interacting w obj directly
    guild_id: int
    install_date: str = str(datetime.now())
    jobs: Optional[List[SheetWatcher]] = field(default_factory=list)

    # Behavior

    def get_job_names(self):
        return [sw.name for sw in self.jobs]

    def add_job(self, sw: SheetWatcher):
        if sw.name in self.get_job_names():
            # TODO see if we just make this overwrite  (FE will handle rest)
            raise APIError('existing SheetWatcher with same name')
        self.jobs.append(sw)

    def pop_job(self, name: str) -> SheetWatcher:
        return self.jobs.pop(self.__get_job_idx(self.get_job(name)))

    def get_job(self, name) -> SheetWatcher:
        try:
            return next(sw for sw in self.get_jobs() if sw.name == name)
        except StopIteration:
            raise APIError('No SheetWatcher with matching name')

    def __get_job_idx(self, sw) -> int:
        try:
            return next(i for i in range(len(self.jobs)) if self.jobs[i] == sw)
        except StopIteration:
            raise APIError('No SheetWatcher with matching name')

    def get_jobs(self) -> List[SheetWatcher]:
        return self.jobs

    def get_updates(self) -> List[Cell]:
        cells = []
        for j in self.jobs:
            cells.extend(j.get_updates())
        return cells

    # Persistence

    @staticmethod
    def read_from(guild_id: int) -> Instance:
        return Instance.from_local(guild_id)

    @staticmethod
    def from_local(guild_id: int) -> Instance:
        local_path = api.LOCAL_OBJECT_PATH / str(guild_id)
        if local_path.exists():
            with open(local_path, 'r') as fp:
                inst = jsons.loads(fp.read(), Instance)
                return inst
        raise APIError('no matching Instance found')

    def write(self):
        return self.write_local()

    def write_local(self) -> Path:
        local_path = api.LOCAL_OBJECT_PATH / str(self.guild_id)
        if local_path.exists():
            logging.info(
                f'Path {str(local_path)} already exists for Instance {str(self)}, overwriting')
        with open(local_path, 'w') as fp:
            fp.write(jsons.dumps(self))
        return local_path
