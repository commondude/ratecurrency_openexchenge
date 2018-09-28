import requests
import json

url = 'http://127.0.0.1:8000/json'
headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
data = {'usd': 100.20}
print(json.dumps(data))
answer = requests.post(url, data=json.dumps(data))
print(answer)
response = answer.json()
print(response)
# answer = requests.get(url, data=json.dumps(data),headers=headers)
# print(type(answer))
# response = answer.json()
# print(response)
