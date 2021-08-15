"""
CONTROLLER FILE
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()



'''
Defining constants for the API
'''

LOCAL_OBJECT_PATH = 'objects/'
LOCAL_OBJECT_PATH = Path(LOCAL_OBJECT_PATH)

PATHS = [LOCAL_OBJECT_PATH]

def init_paths():
    for p in PATHS:
        if not p.exists():
            p.mkdir()
            print(f'{p} made')
        else:
            print(f'{p} exists')

init_paths()


#@InstanceOp
# make decorator that gives instance automatically + error handling to FE
def add_job():
    return None


mock_db = {}

class InstanceTest:
    id: int
    names: List[str]

    def __init__(self, id):
        self.id = id


def create_instance(id):
    instance = InstanceTest(id)
    mock_db[id] = instance

# create_instance(872714949594583040)

def add_sheet_watcher(id, name):
    print("add sheet watcher")
    print(mock_db)
    print(id in mock_db.keys())
    mock_db[id].names.append(name)
    print(name)


def get_sheet_watchers(id):
    return mock_db[id].names


'''

BOT COMMANDS

add(name, sheetLink, cells, time) - Create a new SheetWatcher with the given properties.

delete(name) - Delete the SheetWatcher with the given name.

show() - Return all active SheetWatchers.

check() - Perform a check on all active SheetWatchers. Return the dead cells associated with each.


REPO COMMANDS

create_instance(guild_id)

add_sheet_watcher(guild_id, name, TrackedSheet, CellRange, time) - add SheetWatcher to Instance

pop_sheet_watcher(guild_id, name) - remove SheetWatcher from Instance

get_sheet_watchers(guild_id) - return all SheetWatchers of Instance

get_updates(guild_id, name) - perform check on SheetWatcher with given name


PUNTED

analytics() - Return data analytics and usage.








'''
