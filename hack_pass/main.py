import requests

r = requests.get('https://google.com')
# print(r.text)
print(r.status_code)
