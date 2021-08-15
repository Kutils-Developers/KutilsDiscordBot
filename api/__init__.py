"""
CONTROLLER FILE
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict
from dotenv import load_dotenv
from pathlib import Path
from api.models import Instance, SheetWatcher
import datetime


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

def create_instance(guild_id):
    # TODO ensure instance of guild is not already present in db
    print(f'Creating instance {guild_id}...')
    instance = Instance(datetime.datetime.now(), guild_id)
    instance.write()


def add_sheet_watcher(guild_id, name, time):
    print(f'Instance {guild_id}: adding {name}...')
    instance = Instance.read_from(guild_id)
    sw = SheetWatcher(name, time)
    instance.add_job(sw)
    instance.write()


def pop_sheet_watcher(guild_id, name):
    print(f'Instance {guild_id}: removing {name}...')
    instance = Instance.read_from(guild_id)
    instance.pop_job(name)
    instance.write()


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
