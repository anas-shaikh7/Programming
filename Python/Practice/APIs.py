import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit() # --> Exit the program completely

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response)
# requests.get(...) -->sends an HTTP GET request to the iTunes search API
# The server responds, and that response has a status code attached to it
# When you print(response), Python doesn't show you the actual data (JSON) — it shows a short summary of the response object, which includes the status code

# print(response.json()) ---> do the following to make this understnadable
# print(json.dumps(response.json(), indent=2))
storage = response.json()

for info in storage["results"]:
    print(info["currency"])