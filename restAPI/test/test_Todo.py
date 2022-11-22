import requests

BASE = "http://127.0.0.1:5000/"

data = {"title":"TestTodo", "description":"this is the first test", "completed":False}
data2 = {"title":"TestNoDesc", "completed":False}

response = requests.get(BASE + "todos")
print(response.json())

new_todo = {"title": "POST-Todo", "description": "This todo was postet with a POST-Request", "completed":True}

response = requests.post(BASE + "todos/post",json=new_todo)
print(response.json())

response = requests.get(BASE + "todos")
print(response.json())

# response = requests.post(BASE + 'todos', json=data)
# print(response.json())

# response = requests.get(BASE + "todos")
# print(response.json())