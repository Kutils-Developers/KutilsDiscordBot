"""
Controller file -- provides functions for the operations of the bot.
"""

from __future__ import annotations

from typing import List
from api.support import APIError
from dotenv import load_dotenv
from pathlib import Path
from api.models import Instance, SheetWatcher
import functools
import logging

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
            logging.info(f'{p} made')
        else:
            logging.info(f'{p} exists')


init_paths()


def instance_op(func):
    """
    Decorator for operations that run on an existing Instance.
    Reads & writes the relevant instance file and handles errors
    """

    @functools.wraps(func)
    def wrapper(inst_key, *args, **kwargs):
        logging.info('-----------------------------------------')
        logging.info(f'EXECUTING COMMAND {func.__name__}')
        logging.debug(f'ARGS: {args}')
        logging.debug(f'KWARGS: {kwargs}')
        logging.info(f'~~~')
        try:
            logging.debug(f'Accessing Instance with id {inst_key}')
            inst = Instance.read_from(guild_id=inst_key)
            logging.info(f'Instance accessed {str(inst)}')
            logging.info(f'Running command')
            func_ret = func(inst, *args, **kwargs)
            logging.debug(f'Writing instance {str(inst)}')
            p = inst.write()
            logging.info(f'Instance written at {str(p)}')
        except Exception as e:
            logging.error(msg=f'Exception when doing InstanceOp: {str(e)}, returning None')
            return None
        logging.info('-----------------------------------------')
        return func_ret or inst

    return wrapper


# Behavior

def create_instance(guild_id) -> Instance:
    # TODO ensure instance of guild is not already present in db
    logging.info(f'Creating and writing instance {guild_id}...')
    instance = Instance(guild_id=guild_id)
    instance.write()
    return instance


@instance_op
def add_sheet_watcher(instance: Instance, name, time):
    sw = SheetWatcher(name=name, utc_offset=time)
    instance.add_job(sw)


@instance_op
def pop_sheet_watcher(instance: Instance, name):
    instance.pop_job(name=name)


@instance_op
def get_sheet_watchers(instance: Instance) -> List[SheetWatcher]:
    sw_str = ''
    for j in instance.get_jobs():
        sw_str += str(j)
    return sw_str

'''
BOT COMMANDS
~~~
add(name, sheetLink, cells, time) - Create a new SheetWatcher with the given properties.
    -> add_sheet_watcher(guild_id, name, sheet_link, cell_ranges, time)

delete(name) - Delete the SheetWatcher with the given name.
    -> pop_sheet_watcher(guild_id, name)

show() - Return all active SheetWatchers.
    -> get_sheet_watchers(guild_id)

check() - Perform a check on all active SheetWatchers. Return the dead cells associated with each.
    -> get_updates(guild_id, name)


REPO COMMANDS
~~~
create_instance(guild_id)

add_sheet_watcher(guild_id, name, sheet_link, cell_ranges, time) - add SheetWatcher to Instance

pop_sheet_watcher(guild_id, name) - remove SheetWatcher from Instance

get_sheet_watchers(guild_id) - return all SheetWatchers of Instance

get_updates(guild_id, name) - perform check on SheetWatcher with given name


PUNTED
~~~
analytics() - Return data analytics and usage.

'''
