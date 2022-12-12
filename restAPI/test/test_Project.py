import requests

BASE = "http://127.0.0.1:5000/api"
PROJECT_BASE = BASE + "/projects"
TODO_BASE = BASE + "/todos"

response = requests.get(PROJECT_BASE + "/getAll")
print(response.json())

project = {"title":"POST-Project","description":"This was posted to post"}
response = requests.post(PROJECT_BASE + "/post", json=project)
print(response.json())

response = requests.put(PROJECT_BASE + "/project/1", json={"title":"updated_Title"})
print(response.json())

response = requests.delete(PROJECT_BASE + "/project/1")
print(response.json())

