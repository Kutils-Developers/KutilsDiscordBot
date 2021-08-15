from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Tuple
from pathlib import Path
from datetime import datetime
from api.dataservices.sheets.utils import Cell
import api
from utils import Status
import jsons


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
    tracked_sheet: TrackedSheet

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

    def __get_job_names(self):
        return [sw.name for sw in self.jobs]

    def add_job(self, sw: SheetWatcher) -> Status:
        if sw.name in self.__get_job_names():
            return Status(500, 'existing SheetWatcher with same name')
        self.jobs.append(sw)
        return Status(200)
    
    def pop_job(self, name: str) -> Tuple[Status, SheetWatcher]:
        idx = next(i for i in range(self.jobs) if self.jobs[i].name == name)
        if idx:
            return Status(200), self.jobs.pop(idx)
        return Status(500, 'No SheetWatcher with matching name'), None

    def get_job(self, name):
        return next(sw for sw in self.jobs if sw.name == name)

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
        return None

    def write(self):
        return self.write_local()

    def write_local(self) -> Path:
        local_path = api.LOCAL_OBJECT_PATH / str(self.guild_id)
        with open(local_path, 'w') as fp:
            fp.write(jsons.dumps(self))
        return local_path