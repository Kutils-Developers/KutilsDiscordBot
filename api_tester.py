"""
Debug the API manually and trigger commands from this interface.
"""
import sys
sys.dont_write_bytecode = True

# Allows for full stacktrace prints
import logging
import coloredlogs
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
coloredlogs.install(level='DEBUG')

import api
from api.models import Instance
import jsons

if __name__ == '__main__':
    logging.info('Running API tester')
    api.create_instance(123)
    api.add_sheet_watcher(123, "rvcord", "1lnL3y9L9E4tOaR8rHRBdIyme1PVoKRudYzSF38B07C0", ['Live Performances!D10:D18'], 10)
    dead_cells = api.get_updates(123, "rvcord")
    for i in dead_cells:
        print(i)
