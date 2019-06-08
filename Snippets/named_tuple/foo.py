from collections import namedtuple

x = namedtuple('Pessoa',['nome','idade'])

p = x('Daniel',19)

print(x)

print(p.nome)
print(p.idade)

del x
####CONVENCAO USAR O MSM NOME

Pessoa = namedtuple('Pessoa',['nome','idade'])

p = Pessoa('Daniel',19)

print(Pessoa)

print(p.nome)
print(p.idade)

#[11:08 PM, 5/28/2019] Giuliano Oliveira: da pra você herdar tbm
#[11:08 PM, 5/28/2019] Giuliano Oliveira: tipo class User(namedtuple("User",["nome","senha"])

print('nome: {}, idade:{}'.format(p.nome,p.idade))
print('nome: {nome}, idade:{idade}'.format(nome=p.nome,idade=p.idade))

person = {'name':'daniel', 'age': 19}
print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))
