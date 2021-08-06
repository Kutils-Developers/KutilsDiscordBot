from typing import List, Optional, int, str, long

class CellRange:
    range: List[List[int]]

class TrackedSheet:
    sheet: str
    cell_ranges: List[CellRange]

class SheetWatcher:
    tracked_sheet: TrackedSheet
    utc_offset: long

class Instance:
    install_date: str
    server_id: int
    jobs: List[SheetWatcher]

    def __init__(self):
        x = 0

    def write(self):
        # write to mongo




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








