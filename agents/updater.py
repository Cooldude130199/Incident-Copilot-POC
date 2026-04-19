import requests
from requests.auth import HTTPBasicAuth
from config import INSTANCE_URL, USERNAME, PASSWORD

def update_incident(sys_id, note):
    url = f"{INSTANCE_URL}/api/now/table/incident/{sys_id}"
    auth = HTTPBasicAuth(USERNAME, PASSWORD)
    data = {"comments": note}
    response = requests.patch(url, auth=auth, json=data)
    return response.status_code
