import requests

response = requests.get('https://randomuser.me/api/')

# check the API  connection if 200 its connected
print(response)
print(response.status_code)

# read the json
print(response.json())

# read specific data
gender = response.json()['results'][0]['gender']
print(gender)

title = response.json()['results'][0]['name']['title']
firs_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
print(f"{title}.{firs_name} {last_name}")

age = response.json()['results'][0]['dob']['age']
print(age)