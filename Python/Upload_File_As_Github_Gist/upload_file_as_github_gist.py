'''
This gist is generated by Python.
'''

#!/usr/bin/env python

import requests
import json

GITHUB_API="https://api.github.com"
API_TOKEN='your-token-goes-here'

# form a request URL
url = f"{GITHUB_API}/gists"
print(f"Request URL: {url}")

# print headers,parameters,payload
headers = {'Authorization': f'token {API_TOKEN}'}
params={'scope':'gist'}
payload={"description":"GIST created by python code","public":True,"files":{"Gist by Python":{"content":"This gist is created by Python."}}}

# make a requests
res=requests.post(url,headers=headers,params=params,data=json.dumps(payload))

# print response --> JSON
print(res.status_code)
print(res.url)
print(res.text)
j=json.loads(res.text)

# Print created GIST's details
for _ in range(len(j)):
 print(f"Gist URL : {j['url']}")
 print(f"GIST ID: {j['id']}")
