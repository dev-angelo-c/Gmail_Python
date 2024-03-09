import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# set up credentials
creds = Credentials.from_authorized_user_file('credentials3.json', ['https://www.googleapis.com/auth/gmail.modify'])

# create Gmail API client
service = build('gmail', 'v1', credentials=creds)

# retrieve all read messages
query = "is:read"
messages = service.users().messages().list(userId='me', q=query).execute().get('messages', [])

print(f"found {len(messages)}")

# delete read messages
for message in messages:
    service.users().messages().delete(userId='me', id=message['id']).execute()

print(f"{len(messages)} read messages deleted from your Gmail account.")