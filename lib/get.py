import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"
response = requests.get(url)

json_content = json.loads(response.text)

# format the json in a more readable manner
print(json.dumps(json_content, indent=4))

# print(response.text)  
# print(response.content)
# print(json_content)