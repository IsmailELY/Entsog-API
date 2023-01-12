import requests
import json
payload = {"limit":"-1",}
r = requests.get("https://transparency.entsog.eu/api/v1/connectionpoints", params=payload)

CP_json = r.json()
print(json.dumps(CP_json, indent=2))