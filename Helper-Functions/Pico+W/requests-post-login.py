import requests

payload = {'username': 'mark', 'password': 'test'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
