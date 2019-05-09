import requests, json

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
#200
print(r.headers['content-type'])
#'application/json; charset=utf8'
print(r.encoding)
#'utf-8'
print(r.text)
#u'{"type":"User"...'
print(r.json())
#{u'private_gists': 419, u'total_private_repos': 77, ...}

dict_r = r.json()

print(dict_r)