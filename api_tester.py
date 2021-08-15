"""
Debug the API manually and trigger commands from this interface.
"""
import sys
sys.dont_write_bytecode = True

# Allows for full stacktrace prints
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

import api
from api.models import Instance
import jsons

if __name__=='__main__':
    print('Running API tester')
    api.create_instance(123)
    api.add_sheet_watcher(123, 'hi', 10)
    api.pop_sheet_watcher(123, 'hi')
