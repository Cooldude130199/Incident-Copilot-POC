import requests
from requests.auth import HTTPBasicAuth

url = "https://dev322873.service-now.com/api/now/table/incident"
auth = HTTPBasicAuth("admin", "xgO4Ze$l^R1T")

params = {
    'sysparm_limit': 5,
    'sysparm_fields': 'number,short_description,priority,assignment_group,state,sys_created_on,comments'
}

response = requests.get(url, auth=auth, params=params)
print(response.json())
