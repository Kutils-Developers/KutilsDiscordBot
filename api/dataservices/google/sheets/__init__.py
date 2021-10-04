from typing import List

from api.dataservices.google import sheets_svc
from api.dataservices.google.sheets.utils import Cell, get_column_alphabetical_index_from_zero_indexed_num

# make a call and get a response
# get cells from a response


HYPERLINK_FIELDS = "sheets/properties/title," \
                   "sheets/data/rowData/values/hyperlink," \
                   "sheets/data/startRow," \
                   "sheets/data/startColumn"


def get_cells(spreadsheet_id: str, ranges: list, fields: str = HYPERLINK_FIELDS, service=sheets_svc) -> List[Cell]:
    """Extract cells from Sheet response of Google Sheets API V4"""
    def get_resource():
        """Retrieve a Google Sheets response in JSON"""
        result = service.spreadsheets().get(
            spreadsheetId=spreadsheet_id,
            ranges=ranges,
            fields=fields
        ).execute()
        return result

    result = get_resource()

    cells = []
    for sheet in result['sheets']:
        sheet_name = sheet['properties']['title']
        for a_range in sheet['data']:
            col_alpha = get_column_alphabetical_index_from_zero_indexed_num(a_range['startColumn'])
            row_idx = a_range['startRow'] + 1 if 'startRow' in a_range else 1
            row_data = a_range['rowData']
            for i in range(len(row_data)):
                cell_data = row_data[i]
                if cell_data:
                    c = Cell(sheet_name, row_idx + i, col_alpha, cell_data)
                    cells.append(c)
    return cells
