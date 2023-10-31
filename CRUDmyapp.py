import requests
import json

URLGET ="http://127.0.0.1:8000/siteget/"
URLPOST ="http://127.0.0.1:8000/sitepost/"
URLPUT ="http://127.0.0.1:8000/siteput/"
URLDELETE ="http://127.0.0.1:8000/sitedelete/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URLGET,data = json_data)
    data = r.json()
    print(data)

get_data(1)


def post_data():
    data = {'id':5, 'SiteID': 'MUB2', 'HouseNumber': '59', 'ApartmentNumber': 'RaghuRaghvendra Nagar', 'Landmark': 'RBI Layout', 'City': 'Mumbai', 'State': 'Maharastra', 'PIN': 560078, 'Latitude': 19.0, 'Longtitude': 23.0}
    json_data = json.dumps(data)
    r = requests.post(url=URLPOST,data = json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {'id':4, 'SiteID': 'MUB1', 'HouseNumber': '49', 'ApartmentNumber': 'RaghuRaghvendra Nagar', 'Landmark': 'RBI Layout', 'City': 'Mumbai', 'State': 'Maharastra', 'PIN': 560078, 'Latitude': 19.0, 'Longtitude': 23.0}

    json_data = json.dumps(data)
    r = requests.put(url=URLPUT,data = json_data)
    print(json_data)
    # print(r.text)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {'SiteID':'BLR2'}
    json_data = json.dumps(data)
    print(json_data)
    r = requests.delete(url=URLDELETE,data = json_data)
    data = r.json()
    print(data)
    # print("Status Code:", r.status_code)
    # print("Response Headers:", r.headers)
    # print(r.text)
    # try:
    #     data = r.json()
    #     print(data)
    # except json.JSONDecodeError as e:
    #     print("JSON decoding error:", e)


# delete_data()