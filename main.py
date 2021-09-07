# Using python to communicate with REST API's

# Importing the requests module

import requests

# defining the api_url for the request

api_url = "https://jsonplaceholder.typicode.com/todos/10"
# creating a variable to store the GET request from the api
response = requests.get(api_url)
# formatting the response as a JSON object
print(response.json())

# creating new attributes for the PUT request
todo = {"userId": 2, "title": "Wash Car", "completed": True}
# making the PUT requests with the variable todo
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)

# Using the PATCH method to modify the value of a field
todo = {"title": "Mow Lawn", "id": 15} # changing the value of title and id
response = requests.patch(api_url, json=todo)
print(response.json())

# Using the DELETE request
response = requests.delete(api_url)
print(response.json())
