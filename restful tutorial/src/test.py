import requests

BASE = "http://127.0.0.1:5000/"

data = {"name":"FlaskAPI", "views":69, "likes":42}

response = requests.get(BASE + "videos")
print(response.json())


response = requests.post(BASE + 'videos', json=data)
print(response.json())

response = requests.get(BASE + "videos")
print(response.json())