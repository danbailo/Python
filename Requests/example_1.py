# uma requisicao web, é quando a gente solicita algo na internet
# por exemplo, ao entrarmos em algum site, solicitamos um get e caso o mesmo tenha sucesso
# recemos um codigo 200, para especificar que o request foi um sucesso.

# o erro 404 e um erro bem famoso, esse erro indica que nao existe o formulario requisitado

# os requests mais utilizados é o get e o post. o GET é pedir, pegar, solicitar algo.
# o POST é uma resposta, é enviar algo

# logo, quando se solicita algo, é esperado que um codigo 200

import requests

request_error = requests.get('https://www.google.com/asdasdasd')

print(type(request_error))
print(request_error)
print(request_error.status_code)

request_ok = requests.get('https://solyd.com.br')

print(type(request_ok))
print(request_ok)
print(request_ok.status_code)

# print(request_get.text) #exibe o codigo fonte

# request = requests.get('https://g1.com.br/') https error

#request = requests.get('http://g1.com.br/') 200
#print(request.text)

