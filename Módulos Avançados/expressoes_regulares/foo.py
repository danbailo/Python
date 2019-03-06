#Expressões regulares são padrões de correspondência de texto descritos com uma sintaxe formal

#Procurando padrões em texto
#Um dos usos mais comuns para o módulo re é encontrar padrões no texto. 
#Vamos fazer um exemplo rápido de uso do método de busca para encontrar algum texto:

import re

# Lista de padrões para procurar
patterns = ['term1', 'term2']

# Texto para analisar
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"' % (pattern, text))
    
    # Checa por correspondencia
    if re.search(pattern, text):
        print('\n')
        print('Match was found. \n')
    else:
        print('\n')
        print('No Match was found.\n')

#Agora vimos que re.search () irá pegar o padrão, escanear o texto e retornar um 
# objeto ** Match . Se nenhum padrão for encontrado, um **None será retornado. 
# Para dar uma imagem mais clara desse objeto de correspondência, confira a célula abaixo:

# Lista de padrões para procurar
pattern = 'term1'

# Texto para analisar
text = 'This is a string with term1, but it does not have the other term.'

match = re.search(pattern, text)

print(type(match))

#Este objeto ** Match ** retornado pelo método search() é mais do que apenas um Boolean ou None,
# ele contém informações sobre a partida, incluindo a string de entrada original, 
# a expressão regular que foi usada e a localização da correspondência. 
# Vamos ver os métodos que podemos usar no objeto de correspondência:

# Mostra o índuce de ínicio de uma correspondência
print(match.start())

# Mostra o fim
print(match.end())

#Split com expressões regulares
#Vamos ver como podemos dividir com a sintaxe do re. Isso deve parecer semelhante à forma 
#como você usou o método split() com strings.

# Termo onde realizaremos a divisão
split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# Divide a frase
print(re.split(split_term,phrase))

#Observe como re.split() retorna uma lista com o termo removido e os termos na lista são 
# uma versão dividida da seqüência de caracteres.

#Encontrando todas as instâncias de um padrão¶
#Você pode usar re.findall() para encontrar todas as instâncias de um padrão em uma string. 
# Por exemplo:

# Retorna uma lista de todas as correspondências
print(re.findall('match','test phrase match is in middle'))

#Padrão da sintaxe re
# Esta será a maior parte desta palestra sobre o uso de re com Python. 
# As expressões regulares suportam uma grande variedade de padrões simplesmente descobrindo 
# onde uma única seqüência ocorreu.
# Podemos usar metacaracteres juntamente com re para encontrar tipos específicos de padrões.
# Uma vez que estaremos testando múltiplos formas do re, vamos criar uma função que imprimirá 
# resultados, dada uma lista de várias expressões regulares e uma frase para analisar:

def multi_re_find(patterns,phrase):
    '''
    Toma uma lista de padrões regex
    Imprime uma lista de todas as partidas
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %pattern)
        print(re.findall(pattern,phrase))
        print('\n')

# Sintaxe de repetição
# Existem cinco maneiras de expressar a repetição em um padrão:

#  1.) Um padrão seguido por um metacaractere * é repetido zero ou mais vezes.
#  2.) Substitua o * por + e o padrão deve aparecer pelo menos uma vez.
#  3.) Usar ? significa que o padrão aparece zero ou uma vez.
#  4.) Para um número específico de ocorrências, use {m} após o padrão, onde m é substituído pelo número de vezes que o padrão deve repetir.
#  5.) Use {m, n} onde m é o número mínimo de repetições e n é o máximo.
# Agora, veremos um exemplo de cada um destes usando nossa função multi_re_find:

test_patterns = [ 'sd*',     # s seguido de zero ou mais d's
                'sd+',          # s seguido de um ou mais d's
                'sd?',          # s seguido por zero ou um d
                'sd{3}',        # s seguido por três d's
                'sd{1,3}',      # s seguido de dois a três d's
                ]

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dssssdds...sdddd'

multi_re_find(test_patterns,test_phrase)

#Conjuntos de caracteres
#Os conjuntos de caracteres são usados quando você deseja combinar qualquer grupo de caracteres
# na entrada. Os colchetes são usados para construir entradas de conjunto de caracteres. 
# Por exemplo: a entrada [ab] procura as ocorrências de a ou b. Vamos ver alguns exemplos:

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 
                '[sd]',   # s ou d
                's[sd]+'  # s seguido de um ou mais s ou d's
                ]  
            
multi_re_find(test_patterns,test_phrase)

# Exclusão
# Podemos usar ^ para excluir termos incorporando-os na notação de colchetes. 
# Por exemplo: [^ ...] irá combinar qualquer caracter que não esteja nos colchetes. 
# Vamos ver alguns exemplos:

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

#Use [^!.? ] para verificar se há correspondências que não são !,.,? ou espaço. 
# Adicione o + para verificar se a correspondência aparece pelo menos uma vez, isso 
# basicamente se traduz em encontrar as palavras.

print(re.findall('[!.? ]+',test_phrase))
print(re.findall('[^!.? ]+',test_phrase)) #retorna o inverso, logo, sem esses caracteres

# Intervalos de caracteres
# À medida que os conjuntos de caracteres crescem, a digitação de cada caracter que deve (ou não)
# corresponder pode tornar-se muito tediosa. Um formato mais compacto usando intervalos de 
# caracteres permite que você defina um conjunto de caracteres para incluir todos os caracteres 
# contíguos entre um ponto de início e de parada. O formato utilizado é [inicio-fim].
# Os casos de uso comum são para procurar um intervalo específico de letras no alfabeto, 
# como [a-f] retornaria as correspondências com qualquer instância de letras entre a e f.
# 
# Passemos por alguns exemplos:

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=[ '[a-z]+',      # sequências de letras minúsculas
                '[A-Z]+',      # sequências de letras maiúsculas
                '[a-zA-Z]+',   # sequências de letras maiúsculas ou minúsculas
                '[A-Z][a-z]+'] # uma letra maiúscula seguida de letras minúsculas
                
multi_re_find(test_patterns,test_phrase)