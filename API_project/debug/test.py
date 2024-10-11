import creds
api_key = creds.api_key

import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
payload = ''
headers = {
  'Content-Type': 'application/json'
}
conn.request("GET", f"/apiv1/pantry/{api_key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))