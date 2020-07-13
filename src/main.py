import requests

response = requests.get("http://bbc.co.uk")
response.raise_for_status()
print(response.status_code)
print(response.text)
