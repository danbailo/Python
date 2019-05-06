#API - application programming interface
#interface que se comunica com outros programas
#passa parametros e ela retorna

import requests
import json

request = None

try:
    request = requests.get('http://www.omdbapi.com/?apikey=3232c818&t=interstellar')
except Exception as err:
    print('ERROR:',err)
    exit()

print(request)
print(request.text)

dict_request = json.loads(request.text)

print(dict_request)

print(dict_request['Title'])