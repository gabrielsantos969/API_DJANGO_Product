
import requests

# endpoint  =  "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "Arroz",
    "price": 11.99
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)