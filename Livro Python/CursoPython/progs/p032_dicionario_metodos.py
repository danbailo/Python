# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 19:19:25 2019

@author: notebook
"""

#P032: uso de métodos, funções e iteração sobre um dicionário

#(0)-Cria o dicionário (por enquanto sem Belize e Nova Zelândia!)
d = {
	'Brasil': 204450649,
	'França': 64395345,
	'Portugal':10349803,
	'México': 127017224,
	'Uruguai': 3431555,
}

#(1)-Utilizando os métodos
print('* * * 1-Métodos * * *')
print(d)          
print(d.keys())          
print(d.values())          
print('A população estimada do Brasil é: ', d.get("Brasil"))          

#(2)-percorre todos os elementos de "d"
#  a cada iteração, a chave é armazenada em "k" e o valor em "v"
print('----------------------------------------')
print('* * * 2-Percorrendo o dicionário * * *')
for k, v in d.items(): 
    print(k, '->', v)

#(3)-Utilizando as funções built-in: 
#     len(): conta o número de chaves armazenadas no dicionário
#     min(): menor valor de chave
#     max(): maior valor de chave
print('----------------------------------------')
print('* * * 3-Usando funções built-in * * *')
print('Total de chaves: ', len(d))          
print('menor chave: ', min(d))          
print('maior chave: ', max(d))          

#(4)-Combinando dois dicionários: 
print('----------------------------------------')
print('* * * 4-Combinando Dicionários * * *')
d2 = {
	'Belize': 179014,
	'Nova Zelândia':2213123,
}

d.update(d2)
print('dicionário atualizado: ', d)          

#(5)-removendo todos os itens do dicionário
print('----------------------------------------')
print('* * * 5-Destruindo um dicionário * * *')
d.clear()          
print(d)          
