#How to run
# $ python3 getquote.py

import socket
import select
import re

target_host = "i.ytimg.com"

#Link dado em sala de aula, descomente para testar
# target_host = "www.google.com"

target_port = 80
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um objeto do tipo socket
client.connect((target_host,target_port))
target_extension = "/vi/e2jerZDvtG8/maxresdefault.jpg"

#Descomente esse abaixo também, pois é a imagem referente ao host descomentado acima
# target_extension = "/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"

request = "GET %s HTTP/1.1\r\nHost:%s\r\n\r\n" % (target_extension,target_host)
client.send(request.encode())

reply = b''
while select.select([client], [], [], 3)[0]:
    data = client.recv(1024)
    if not data: break
    reply += data
client.close()

#Realizei alguns testes e obtive alguns erros 301 e 404, então fiz essa condição para encerrar o programa caso alguma 
# resposta seja algum desses dois status, pois assim não será criado o arquivo binário contendo "nada".
if not re.search(r"HTTP\/1.1+\s200", str(reply)):
    print('ERROR - status code 200 not obtained. Please, try other link!')
    exit(-1)

headers = reply.split(b'\r\n\r\n')[0]
image = reply[len(headers)+4:]

print('File Downloaded Successfully!\nSearch by "foo.png" in your directory')
#Salva a imagem
with open ('foo.png', 'wb') as f: f.write(image)
