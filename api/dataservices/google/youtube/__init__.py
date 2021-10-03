import logging

import googleapiclient
from api.dataservices.google import youtube_svc

delete_keywords = ['&feature', '&list', '&index', '&lc', '&ab_channel', '&t']

# TODO redo youtube ID extraction with urlparse


def extract_youtube_ids_from_url(url: str) -> str:
    if not is_youtube_video_url(url):
        return
    # TODO figure out what to return

    for kw in delete_keywords:
        if kw in url:
            url = url[:url.find(kw)]

    if is_link_shortened(url) and url.rfind('?') > 0:
        id = url[url.rfind('/') + 1:url.rfind('?')]
    elif is_link_shortened(url):
        id = url[url.rfind('/') + 1:]
        # TODO special chars not in id list
    elif '&' in url:
        id = url[url.rfind('=') + 1:url.find('&')]
    elif ']' in url:
        id = url[url.rfind('=') + 1:url.find(']')]
    else:
        id = url[url.rfind('=') + 1:]

    return id


def is_youtube_video_url(url: str) -> bool:
    # TODO better cleanurl
    return ('playlist' not in url) and ('youtube.com' in url or 'youtu.be' in url) and ('results' not in url)


def is_link_shortened(url: str) -> bool:
    # not necessarily the best b/c of double youtube phenomenon (youtube.com...&feature=youtu.be)
    return 'youtu.be' in url


def is_dead_youtube_link(url: str) -> bool:
    id = extract_youtube_ids_from_url(url)
    request = youtube_svc.videos().list(part="status,contentDetails", id=id)
    print(type(request))
    try:
        response = request.execute()
    except Exception as e:
        logging.debug(url)
        print(e)
        return True

    items = response['items']
    return not len(items) and id


if __name__ == '__main__':
    print(is_dead_youtube_link("https://www.youtube.com/watch?v=icBYTc0ty6A"))
    print("hi")



#    def extract_youtube_ids_from_urls(urls):
#     ids = []
#     count_non_yt_vid = 0
#     for url in urls:
#         if not is_youtube_video_url(url):
#             count_non_yt_vid += 1
#             continue
#
#         for kw in delete_keywords:
#             if kw in url:
#                 url = url[:url.find(kw)]
#
#         if is_link_shortened(url) and url.rfind('?') > 0:
#             id = url[url.rfind('/') + 1:url.rfind('?')]
#         elif is_link_shortened(url):
#             id = url[url.rfind('/') + 1:]
#         # TODO special chars not in id list
#         elif '&' in url:
#             id = url[url.rfind('=') + 1:url.find('&')]
#         elif ']' in url:
#             id = url[url.rfind('=') + 1:url.find(']')]
#         else:
#             id = url[url.rfind('=') + 1:]
#
#         ids.append(id)
#     return ids, count_non_yt_vid