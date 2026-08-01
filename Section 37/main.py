import requests
import dotenv
from datetime import datetime

config = dotenv.dotenv_values(".env")
pixela_endpoint = "https://pixe.la/v1/users"
username = config["USERNAME"]
token = config["PIXELA_TOKEN"]
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_id = "graph1"

# graph_config = {
#     "id": graph_id,
#     "name": "Coding Graph",
#     "unit": "minute",
#     "type": "int",
#     "color": "shibafu",
# }

headers = {
    "X-USER-TOKEN": token,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

pixel_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime.now().strftime("%Y%m%d")
print(today)

pixel_config = {"date": today, "quantity": "60"}
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)
