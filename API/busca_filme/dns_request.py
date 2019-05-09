import socket,requests
ip = socket.gethostbyname('www.omdbapi.com')
print(ip)
# print(type(ip))
#'104.20.134.15'
headers={'Host':'www.omdbapi.com'}
print(headers)
#{'Host': 'www.omdbapi.com'}
res = requests.get('http://%s'%ip,headers=headers)
print(res)
#<Response [200]>


