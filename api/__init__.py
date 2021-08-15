"""
Controller file -- provides functions for the operations of the bot.
"""

from __future__ import annotations
from api.support import APIError
from dataclasses import dataclass
from typing import List, Dict
from dotenv import load_dotenv
from pathlib import Path
from api.models import Instance, SheetWatcher
import datetime
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
            func(inst, *args, **kwargs)
            logging.debug(f'Writing instance {str(inst)}')
            p = inst.write()
            logging.info(f'Instance written at {str(p)}')
        except Exception as e:
            logging.error(msg=f'Exception when doing InstanceOp: {str(e)}, returning None')
            return None
        logging.info('-----------------------------------------')
        return inst

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
    logging.info(f'Instance {instance}: adding {name}...')
    sw = SheetWatcher(name=name, utc_offset=time)
    instance.add_job(sw)


@instance_op
def pop_sheet_watcher(instance: Instance, name):
    logging.info(f'Instance {instance}: removing {name}...')
    instance.pop_job(name=name)


'''
BOT COMMANDS
~~~
add(name, sheetLink, cells, time) - Create a new SheetWatcher with the given properties.

delete(name) - Delete the SheetWatcher with the given name.

show() - Return all active SheetWatchers.

check() - Perform a check on all active SheetWatchers. Return the dead cells associated with each.


REPO COMMANDS
~~~
create_instance(guild_id)

add_sheet_watcher(guild_id, name, TrackedSheet, CellRange, time) - add SheetWatcher to Instance

pop_sheet_watcher(guild_id, name) - remove SheetWatcher from Instance

get_sheet_watchers(guild_id) - return all SheetWatchers of Instance

get_updates(guild_id, name) - perform check on SheetWatcher with given name


PUNTED
~~~
analytics() - Return data analytics and usage.

'''
