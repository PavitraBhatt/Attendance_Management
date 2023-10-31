import requests
import json

URL = "http://127.0.0.1:8000/sitecreate/"

data = {"id":3,"SiteID": "BLR2", "HouseNumber": "99", "ApartmentNumber": "RaghuRaghvendra2 Nagar", "Landmark": "Brigade Mil.", "City": "Bengaluru", "State": "Karnataka", "PIN": 560078, "Latitude": 19.0, "Longtitude": 23.0}

json_data = json.dumps(data)

r= requests.post(url= URL, data = json_data)

data = r.json()
print(data) 