# Pixela API - put datat to pixela
import requests
import datetime

USERNAME = "annaf111"
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "token goes here"

user_params = {
    "token": "hdhdkeossfewedewdeee",
    "username": "anna",
    "agreeTermsOfService": "yes",
    "noMinor": "yes",
}

# new endpoint
graph_endpoint = f"[{pixela_endpoint}/{USERNAME}/graphs"

# Id has to be first letter and later numbers
# It can be any tracking type
graph_config = {
    "id": "graph1",
    "name": "Running graph",
    "unit": "km",
    "type": "float",
    "color": "aiajai"
}

headers = {
    "X_USER_TOKEN": TOKEN
}

# Post the data in pixela
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.datetime(year=2025, month=5, day=4)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you run? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Use put method to update any data
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "64"
}
# response = requests.put(url=pixel_creation_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Use put method to delete any data
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
