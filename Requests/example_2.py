import requests # beautiful soup 4 - selecionar algumas partes do codigo html
#https://putsreq.com/

#cabeçalhos padrão do http, User-agent e um deles
header = {
    'User-agent': 'Fake News!',
    'Referer': 'https//www.google.com/'}

cookie = {'Ultima-visita': '10-10-2020'}

data = {
    'username': 'newbie',
    'password': '123456789'}

text = None
try:
    request = requests.post(
        'https://putsreq.com/lp7fD0HaPE6LnN7MfEFI',
        headers=header,
        cookies=cookie,
        data=data)
    text = request.text
except Exception as err:
    print('ERROR: {}'.format(err))

print(text)

#um metodo para realizar um brute-force, é vc ficar dando um requests.post, é possivel criar essa
# ferramenta para realizar um brute-force, ficar mandando solicitacao post no login , com varios login
# diferente, abrindo num arquivo de word-list