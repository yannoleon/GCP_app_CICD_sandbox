import requests
import json

# Local API endpoint
# url = "http://127.0.0.1:8080"

# Remote API endpoint (don't forget to make it public or to specify authentication auth=(id, pw) in the post method)
url = "https://helloworld-594819012176.us-central1.run.app/summation"

# Send a request to the API
query = json.dumps({
  "a": 1., "b": 2
})
response = requests.post(url, query)

# response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.content
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
