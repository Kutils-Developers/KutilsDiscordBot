from urllib.parse import urlparse


def get_twitter_id_from_url(url: str) -> str:
    url_path = urlparse(url)[2]
    raw_username = url_path[1:]
    if '/' in raw_username:
        un = raw_username[:raw_username.find('/')]
    else:
        un = raw_username
    return un


# def get_twitter_id_to_cells(cells: list) -> dict:
#     twitter_to_cell = {}
#     for c in cells:
#         c: Cell
#         cell, id = c.get_cell_url_relation(get_twitter_id_from_url)
#         twitter_to_cell[id] = cell
#     return twitter_to_cell


def is_twitter_account_url(url: str) -> bool:
    return "twitter.com" in url
