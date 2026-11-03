import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()
# possible sys.argv[1] = Programming, dark
response = requests.get("https://v2.jokeapi.dev/joke/" + sys.argv[1])
# print(json.dumps(response.json(), indent=3))

jokes = response.json()
print(jokes["setup"])
print(jokes["delivery"])
