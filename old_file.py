
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# TEST DELETE BEFORE PULL (LEARN GIT HUB ON PYCHARM)


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph (Testing)",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

date_now = datetime(year=2021, month=6 ,day=2)
date = date_now.strftime("%Y%m%d")
print(date)


post_config = {
    "date": date,
    "quantity": "100"
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)


put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"

put_config = {
    "quantity": "10"
}
# TEST DELETE BEFORE PULL (LEARN GIT HUB ON PYCHARM)
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"
# response = requests.delete(url=put_endpoint, headers=headers)
# print(response.text)
