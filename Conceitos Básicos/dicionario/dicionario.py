#listas são sequencias
#dicionarios são mapeamentos
#pode pensar nestes Dicionários como tabelas de hash.

#Os mapeamentos são uma coleção de objetos que são armazenados por uma chave, ao contrário 
#de uma seqüência que armazena objetos por sua posição relativa. Esta é uma distinção importante
#uma vez que os mapeamentos não reterão a ordem, pois possuem objetos definidos por uma chave.

#Um dicionário de Python consiste em uma chave e depois em um valor associado. 
#Esse valor pode ser quase qualquer objeto Python.

# Cria um dicionário com {} e: que significa uma chave e um valor
my_dict = {'key1':'value1','key2':'value2'}

print(type(my_dict))

print(my_dict)

# Chamando valores pela chave
print(my_dict['key1'])

#É importante notar que os dicionários são muito flexíveis com relação aos tipos de dados que eles podem conter.
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict)

# Vamos chamar itens do dicionário
print(my_dict['key3'])

# Podemos chamar itens de uma lista presente na posição referente à chave 'key3'
print(my_dict['key3'][1])

#com isto podemos usar todos os métodos presentes em listas, ex:
print(my_dict['key3'][0].upper())

#Podemos também alterar valores através da chave.
print(my_dict['key1'])

my_dict['key1'] -= 200

print(my_dict['key1'])

print('\n')
#Também podemos criar chaves por atribuição. Por exemplo, se começássemos com um
#dicionário vazio, poderíamos adicionar-lhe continuamente:

#cria um novo dicionario
d = {}

print(type(d))
print(d)

# Cria uma chave por associoação
d['animal'] = 'cachorro'
print(d)

# Pode fazer isso com qualquer objeto
d['answer'] = 42
print(d)

d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d)

# Continue chamando as chaves...
print(d['key1']['nestkey']['subnestkey'])

#Alguns métodos de dicionários
print('\nAlguns métodos de dicionarios')

# Cria um dicionário típico
d = {'key1':1,'key2':2,'key3':3}
print(d)

# Retorna uma lista de todas as chaves
print('keys: ',d.keys())

# Pega todos os valores
print(d.values())

# Método para retornar as tuplas de todos os itens (aprenderemos sobre as tuplas em breve)
print(d.items())

print('\nCompreensão em dicionarios')

x = {x:x**2 for x in range(10)}

print(x)

#Iteração sobre chaves, valores e itens

#Os dicionários podem ser iterados ao usar os métodos iterativos disponíveis em um dicionário

d = {'key1':1,'key2':2,'key3':3}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for item in d.items():
    print(item)

account_balance={}

# account_number = str(input())
# deposit = float(input('Input a value of deposit: '))
# account_balance[account_number] = deposit 

# for item in account_balance.items():
#     print(item)

#     print('Please, input a number of account: ')    
#     account_number = str(input())
#     # print(len(account_number))

#     while len(account_number) != 6 or account_number in account_balance:
#         if len(account_number) != 6:
#             print('Account must have 6 numbers: ')
#         elif account_number in account_balance:
#             print('This account has exist in bank, input a different number: ')
#         account_number = str(input())
        
#         deposit = float(input('Input a value of deposit: '))
#         account_balance[account_number] = deposit 

del d

print('\nhere')

d = {}

d['daniel'] = []
print(d)
d['daniel'].append('lucas')
print(d)
d['daniel'].append('josue')
print(d)

for v in d.values():
    print(v)     
    print('%s' % v[0])

del d


print('\ntesting here')
d = {}

d[('key1',1)] = 'daniel'
d[('key2',2)] = 'josue'
d[('key3',3)] = 'lucas'

print(d['key1',1])
print(d[('key1',1)][0])

print(d.values())

print(('tupla',1))
print(('mesma tupla',1)[0])

if ('key1',1)[0] in d.keys():
	print('ok')