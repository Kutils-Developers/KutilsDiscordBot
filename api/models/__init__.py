from __future__ import annotations

from dataclasses import dataclass
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
    utc_offset: int
    tracked_sheet: TrackedSheet


@dataclass
class Instance:
    """Bot Instance API Object. Assumes that Instances are uniquely defined by guild_id"""
    install_date: str
    guild_id: int
    jobs: Optional[Dict[str, SheetWatcher]] = {}

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

    # Behavior

    def add_job(self, sw: SheetWatcher, name: str) -> Status:
        if name in self.jobs.keys():
            return Status(500, 'existing SheetWatcher with same name')
        self.jobs[name] = sw
        return Status(200)
    
    def pop_job(self, name: str) -> Tuple[Status, SheetWatcher]:
        if name in self.jobs.keys():
            return self.jobs.pop(name), Status(200)
        return Status(500, 'No SheetWatcher with matching name')

