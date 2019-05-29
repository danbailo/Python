import re

exampleString = '''
Jessica is 9 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''

string = 'Jessica is 9 years old, and Daniel is 27 years old.'

print(exampleString)
#\d{1,3} digito decimal com tamanho de 1,2 ou 3
ages = re.compile('\d{1,3}').split(string)
print(ages)

#comeca com uma letra maiscula e pode ter varias minusculas
names = re.findall(r'[A-Z][a-z]*',exampleString)
print(names)

string = 'HELLO there HOW are YOU'
new_string = re.split(r'(?<!^)\s+(?=[A-Z])(?!.\s)',string)
print(new_string)

print()

xx = 'guru99,education is fun'
r1 = re.findall(r'\D+', xx)
print(r1)
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's','split the words')))

print(re.compile('(?:[^\\s"]+|"[^"]*")+').findall('mv "batata assada" da'))