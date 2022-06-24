import requests

rss = requests.get('https://httpbin.org/basic-auth/path/path',auth=('path','path'))
print(rss.json())
print(rss.status_code)
print(rss.headers)