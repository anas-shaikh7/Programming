import requests
import json

response = requests.get("https://openlibrary.org/search.json?q=harry+potter")
# print(json.dumps(response.json(), indent=2))
container = response.json()

for data in container["docs"]:
    print(data["title"])