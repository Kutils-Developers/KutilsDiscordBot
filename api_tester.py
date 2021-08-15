"""
Debug the API manually and trigger commands from this interface.
"""

import api
from api.models import Instance
import jsons

if __name__=='__main__':
    print('Running API tester')
    inst = Instance('2021', 124)
    inst = Instance()
