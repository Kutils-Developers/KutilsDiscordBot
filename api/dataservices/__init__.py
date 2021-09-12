import googleapiclient

from api.dataservices.google.sheets import get_cells
from api.dataservices.google import sheets_svc, youtube_svc
from api.dataservices.google.youtube import extract_youtube_ids_from_urls


def get_dead_cells(sheet_id, sheet_ranges):
    # construct relevant cells
    cells = get_cells(sheets_svc, sheet_id, sheet_ranges)




