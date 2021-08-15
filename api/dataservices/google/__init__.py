import os
from typing import List
from googleapiclient.discovery import build
from google.oauth2 import service_account
from pathlib import Path

default_google_scopes = ['https://www.googleapis.com/auth/youtube.readonly',
                         "https://www.googleapis.com/auth/spreadsheets.readonly"]

GOOGLE_SERVICES = {'youtube': ['youtube', 'v3'], 'sheets': ['sheets', 'v4']}


def get_google_credentials(scopes: List[str] = default_google_scopes):
    return service_account.Credentials.\
        from_service_account_file(Path(os.environ('GOOGLE_SVC_CREDENTIALS')))


def build_service(svc_key: str, credentials=get_google_credentials()):
    return build(GOOGLE_SERVICES[svc_key][0], GOOGLE_SERVICES[svc_key][1], credentials)