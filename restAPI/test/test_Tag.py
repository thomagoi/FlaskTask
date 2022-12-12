import requests

BASE = "http://127.0.0.1:5000/api/tags"
TODO_BASE = "http://127.0.0.1:5000/api/todos"

response = requests.get(BASE + "/getAll")
print(response.json())

print("----------------------------")
print("create Tag with some todos:")
print("----------------------------")

new_tag = {"name":"POST-tag"}

new_todo1 = {"title":"Todo1", "description":"test Todo to test Tag", "tag":1}
new_todo2 = {"title":"Todo2", "description":"test Todo to test Tag", "tag":1}

response = requests.post(BASE + "/post",json=new_tag)
print(response.json(), response.status_code)

reponse = requests.post(TODO_BASE + "/post",json=new_todo1)
reponse = requests.post(TODO_BASE + "/post",json=new_todo2)

print("----------------------------")
print("try to get specific tag:")
print("----------------------------")

response = requests.get(BASE + "/tag/1")
print(response.json(), response.status_code)

print("----------------------------")
print("try to get todos of specific tag:")
print("----------------------------")

response = requests.get(BASE + "/tag/1/todos")
print(response.json(), response.status_code)

print("----------------------------")
print("try update specific tag:")
print("----------------------------")

update_dict = {"name":"new_name"}
response = requests.put(BASE + "/tag/1",json=update_dict)
print(response.json(),response.status_code)

print("----------------------------")
print("try delete specific tag:")
print("----------------------------")
response = requests.delete(BASE + "/tag/1")
print(response.json(),response.status_code)

print("----------------------------")
print("look at formerly linked todos:")
print("----------------------------")

response = requests.get(TODO_BASE + "/todo/1")
print(response.json(),response.status_code)

assert response.json()['tag'] is None 

response = requests.delete(TODO_BASE + "/todo/1")
response = requests.delete(TODO_BASE + "/todo/2")

print("----------------------------")
print("return list of all tags:")
print("----------------------------")
response = requests.get(BASE + "/getAll")
print(response.json())

