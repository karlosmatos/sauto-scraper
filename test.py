import requests
import json


url = "https://www.sauto.cz/api/v1/items/search"

req = requests.get(url, verify=False)

print(req.headers)