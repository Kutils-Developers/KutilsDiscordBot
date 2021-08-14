from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Dict
from pathlib import Path
from datetime import datetime

from api.dataservices.sheets.utils import Cell
from utils import Status


@dataclass
class Instance:
    install_date: str
    server_id: int
    channel: str
    jobs: Dict[SheetWatcher]

    def add_job(self, sw: SheetWatcher, name: str) -> Status:
        if name in self.jobs.keys():
            return Status(500, 'existing SheetWatcher with same name')
        self.jobs[name] = sw
        return Status(200)




@dataclass
class SheetWatcher:
    tracked_sheet: TrackedSheet
    utc_offset: int


@dataclass
class TrackedSheet:
    sheet: str
    cell_ranges: List[CellRange]


@dataclass
class CellRange:
    range: List[List[Cell]]