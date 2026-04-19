import requests
from requests.auth import HTTPBasicAuth
from config import INSTANCE_URL, USERNAME, PASSWORD

def fetch_incidents(limit=10):
    url = f"{INSTANCE_URL}/api/now/table/incident"
    auth = HTTPBasicAuth(USERNAME, PASSWORD)
    params = {
        'sysparm_limit': limit,
        'sysparm_fields': 'number,short_description,priority,assignment_group,state,sys_created_on,comments'
    }
    response = requests.get(url, auth=auth, params=params)
    return response.json().get("result", [])
