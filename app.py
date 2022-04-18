import requests

response = requests.get("https://swapi.dev/api/people/1/")

print(response.text)
