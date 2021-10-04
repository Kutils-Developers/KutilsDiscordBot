from dataclasses import dataclass
from typing import Optional

from api.dataservices.google.youtube import is_dead_youtube_link
from api.dataservices.utils import which_service


class Cell:
    sheet: str
    row_idx: int
    col_idx: int
    data: str
    svc_type: str

    def __init__(self, sheet, row_idx, col_idx, data):
        self.sheet = sheet
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.data = data
        self.svc_type = which_service(self.get_url())

    def get_url(self):
        if 'hyperlink' not in self.data['values'][0]:
            print(self.__str__() + " has error")
            return
        return self.data['values'][0]['hyperlink']

    def is_dead(self):
        if self.svc_type == "youtube":
            return is_dead_youtube_link(self.get_url())

    def __str__(self):
        return self.sheet + ' ' + self.col_idx + str(self.row_idx)


def get_column_alphabetical_index_from_zero_indexed_num(col_idx: int) -> str:
    """Convert zero-index column number to alphabetical base-26 (e.g. 0 -> 'A', 27 -> 'AA'"""
    num_letters_alphabet = 26

    def get_letter_from_zero_indexed_idx(idx: int):
        ascii_start = 65
        return chr(ascii_start + idx)

    prefix_str = ''
    if col_idx < num_letters_alphabet:
        return get_letter_from_zero_indexed_idx(col_idx)
    last_char = get_letter_from_zero_indexed_idx(col_idx % num_letters_alphabet)
    prefix_str = get_column_alphabetical_index_from_zero_indexed_num(col_idx // num_letters_alphabet)
    return prefix_str + last_char
