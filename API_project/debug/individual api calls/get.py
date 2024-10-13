import sys, os, http.client, json
sys.path.append(os.path.abspath('API_project'))
import creds
api_key = creds.api_key



conn = http.client.HTTPSConnection("getpantry.cloud")
payload = ''
headers = {
		'Content-Type': 'application/json'
}
conn.request("GET", f"/apiv1/pantry/{api_key}/basket/pantry1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))