from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional
from pathlib import Path
from datetime import datetime
from api.dataservices.google.sheets.utils import Cell
from api.support import APIError
import api
import jsons
import logging


@dataclass
class CellRange:
    range: List[List[Cell]]


@dataclass
class TrackedSheet:
    sheet: str
    cell_ranges: List[CellRange]


@dataclass
class SheetWatcher:
    """Assumes that a SheetWatcher is uniquely defined by their name"""
    name: str
    utc_offset: int
    tracked_sheet: Optional[TrackedSheet] = None

    def __eq__(self, other):
        if type(other) == type(self):
            return other.name == self.name
        return False


@dataclass
class Instance:
    """Bot Instance API Object. Assumes that Instances are uniquely defined by guild_id"""
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
        try:
            idx = next(i for i in range(len(self.jobs))
                       if self.jobs[i].name == name)
            return self.jobs.pop(idx)
        except StopIteration:
            raise APIError('No SheetWatcher with matching name')

    def get_job(self, name):
        try: 
            return next(sw for sw in self.jobs if sw.name == name)
        except StopIteration:
           raise APIError('No SheetWatcher with matching name')
    
    def get_jobs(self):
        return self.jobs

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
            logging.warning(
                f'Path {str(local_path)} already exists for Instance {str(self)}, overwriting')
        with open(local_path, 'w') as fp:
            fp.write(jsons.dumps(self))
        return local_path
