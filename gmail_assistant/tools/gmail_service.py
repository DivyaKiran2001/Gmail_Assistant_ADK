
"""
   Utility functions for Gmail API integration. 
"""

import os
import json
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledFlow
from googleapiclient.discovery import build

# Define scopes for Gmail
SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
]

# Paths for credentials
TOKEN_PATH = Path(os.path.expanduser("~/.credentials/gmail_token.json"))
CREDENTIALS_PATH = Path("credentials/service_account.json")  # or credentials.json

def get_gmail_service_via_oauth():
    
    """
        Authenticate using OAuth (installed app flow).

        Returns:
            Gmail API service object or None
    """
    creds=None

    # Check if token exists and is valid
    if TOKEN_PATH.exists():
        creds=Credentials.from_authorized_user_info(
            json.loads(TOKEN_PATH.read_text()),SCOPES
        )
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_PATH.exists():
                print("Missing credentials file.")
                return None
            flow = InstalledFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds= flow.run_local_server(port=0)
        TOKEN_PATH.parent.mkdir(parents=True,exist_ok=True)
        TOKEN_PATH.write_text(creds.to_json())

    return build("gmail","v1",credentials=creds)



