import os
import requests
import asyncio

AIRTABLE_BASE_ID=os.environ.get('AIRTABLE_BASE_ID')
AIRTABLE_API_KEY=os.environ.get('AIRTABLE_API_KEY')
AIRTABLE_TABLE_NAME=os.environ.get('AIRTABLE_TABLE_NAME')

def push(quotes=None):
    if quotes is None:
        return False
    endpoint = f"https://api.airtable.com/v0/appnzVzlJ8whH9u8P/scheduled_tasks"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "records": [
            {
            "fields": {
                "quotes": quotes,
            }
            }
        ]
    }

    r = requests.post(endpoint,json=data, headers=headers)
    print(r.json())
    return r.status_code == 200

def get():

    endpoint = f"https://api.airtable.com/v0/appnzVzlJ8whH9u8P/scheduled_tasks"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "maxRecords":"100",
        "view":"Grid view"
    }

    r = requests.get(endpoint, headers = headers, params = params )

    response = []
    for item in r.json()['records']:
        response.append(item['fields'].get('quotes'))
    return response