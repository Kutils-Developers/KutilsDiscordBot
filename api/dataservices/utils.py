from api.dataservices.google.youtube import is_youtube_video_url
from api.dataservices.google.twitter import is_twitter_account_url


def which_service(url: str) -> str:
    if is_youtube_video_url(url):
        return "youtube"
    if is_twitter_account_url(url):
        return "twitter"
