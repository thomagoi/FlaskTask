import requests

BASE = "http://127.0.0.1:5000/api/"

# data = {"title":"TestTodo", "description":"this is the first test", "completed":False}
# data2 = {"title":"TestNoDesc", "completed":False}

response = requests.get(BASE + "todos/getAll")
print(response.json())

print("----------------------------")
print("post a new todo:")
print("----------------------------")

new_todo = {"title": "POST-Todo", "description": "This todo was posted with a POST-Request", "completed":True}

response = requests.post(BASE + "todos/post",json=new_todo)
print(response.json(),response.status_code)

print("----------------------------")
print("try to get specific todo:")
print("----------------------------")

response = requests.get(BASE + "todos/todo/1")
print(response.json(),response.status_code)

response = requests.get(BASE + "todos/todo/4")
print(response.json(),response.status_code)

print("----------------------------")
print("update todo:")
print("----------------------------")

update_dict = {"title":"updated_title","description":"This todo was updated","test":"This should still work"}
response = requests.put(BASE + "todos/todo/1",json=update_dict)
print(response.json(),response.status_code)

print("----------------------------")
print("delete posted todo:")
print("----------------------------")

response = requests.delete(BASE + "todos/todo/1")
print(response.json(), response.status_code)

print("----------------------------")
print("return list of all todos:")
print("----------------------------")
response = requests.get(BASE + "todos/getAll")
print(response.json())