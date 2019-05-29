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