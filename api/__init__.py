from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict
from dotenv import load_dotenv


load_dotenv()


mock_db = {}

class InstanceTest:
    id: int
    names: List[str]

    def __init__(self, id):
        self.id = id


def create_instance(id):
    instance = InstanceTest(id)
    mock_db[id] = instance

create_instance(872714949594583040)

def add_sheet_watcher(id, name):
    print("add sheet watcher")
    print(mock_db)
    print(id in mock_db.keys())
    mock_db[id].names.append(name)
    print(name)


def get_sheet_watchers(id):
    return mock_db[id].names





'''
PUBLIC (DISCORD BOT)

create_instance(server_id)
- > Instance.__init__

add_sheet_watcher(name, Instance, TrackedSheet, time)


Bot commands


add(name, sheetLink, cells, time) - Create a new SheetWatcher with the given properties.

add_sheet_watcher(name, Instance, TrackedSheet, time)

delete(name) - Delete the SheetWatcher with the given name.

pop_watcher(Instance, name) - remove SheetWatcher from Instance

show() - Return all active SheetWatchers.

get_sheetwatchers(Instance)

check() - Perform a check on all active SheetWatchers. Return the dead cells associated with each.

get_updates(Instance)

analytics() - Return data analytics and usage.

# punt


PRIVATE (API)

createBot(id, Schedules[]) - Create a Bot object and store into database.

checkSheet(id, name) - Perform a check on the Scheduler with the given name under the Bot with the given id.

addScheduler(id, Scheduler) - add Scheduler to Bot with given id.

deleteScheduler(id, name) - delete Scheduler with given name from Bot with given id.

getSchedulers(id) - Return the Schedulers under the Bot with the given id.

analytics() - Return data analytics and usage.


Bot commands







'''
