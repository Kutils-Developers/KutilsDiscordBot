from dataclasses import dataclass


@dataclass
class Cell:
    sheet = None
    row_idx = 0
    col_idx = ''
    data = None

    def get_url(self):
        if 'hyperlink' not in self.data['values'][0]:
            print(self.__str__() + " has error")
        return self.data['values'][0]['hyperlink']

    def get_cell_url_relation(self, url_data_extractor):
        return self, url_data_extractor(self.get_url())

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