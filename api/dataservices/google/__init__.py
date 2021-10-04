import os
from typing import List
from googleapiclient.discovery import build
from google.oauth2 import service_account
from pathlib import Path
import logging

from dotenv import load_dotenv
load_dotenv()


DEFAULT_GOOGLE_SCOPES = ['https://www.googleapis.com/auth/youtube.readonly',
                         "https://www.googleapis.com/auth/spreadsheets.readonly"]

GOOGLE_SERVICES = {'youtube': ['youtube', 'v3'], 'sheets': ['sheets', 'v4']}


def get_google_credentials(scopes: List[str] = DEFAULT_GOOGLE_SCOPES):
    return service_account.Credentials.\
        from_service_account_file(Path(os.environ['GOOGLE_CRED_JSON']), scopes=scopes)


def build_service(svc_key: str, credentials=get_google_credentials()):
    return build(GOOGLE_SERVICES[svc_key][0], GOOGLE_SERVICES[svc_key][1], credentials=credentials)


sheets_svc = build_service('sheets')
youtube_svc = build_service('youtube')
logging.info('services building...')

