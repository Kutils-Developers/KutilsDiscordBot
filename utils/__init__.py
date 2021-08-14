# load vars
from typing import Dict

from dotenv import load_dotenv

load_dotenv()


class Status:
    code: int
    stat_dict: Dict[int, str] = {
        200: 'OK',
        400: 'CLIENT ERROR',
        500: 'SERVER ERROR'
    }
    msg: str

    def __init__(self, code, msg=None):
        self.code = code
        self.msg = msg

    def __str__(self):
        if self.msg:
            return f'STATUS {self.code}: ({self.stat_dict[self.code]}) {self.msg}'
        return

    def __eq__(self, other):
        if type(other) is int:
            if other in self.stat_dict.keys():
                return self.code == other
        elif type(other) is Status:
            return self.code == other.code
        return False
