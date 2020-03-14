import requests

# get 方式
r = requests.get('http://httpbin.org/get', headers={'user-agent': 'safari'})

# post 方式
r= requests.post('http://httpbin.org/post', data={'key': 'safari'})
print(r.json())
