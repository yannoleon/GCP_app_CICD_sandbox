import requests

# API endpoint (don't forget to make it public or to specify authentication auth=(id, pw) in the post method)
url = "http://127.0.0.1:8080/summation"

query = {
  "a": 1., "b": 2
}
response = requests.post(url, json=query, timeout=60)

# response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.content
    print(data.decode('utf-8'))
else:
    print(f"Failed to retrieve data: {response.status_code}")
