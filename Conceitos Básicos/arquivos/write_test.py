#https://docs.python.org/3/library/functions.html#open

file = open('test.csv','w+', encoding='UTF-8')

file.write('testando\n')
file.write('1\n')
file.write('2\n')
file.write('tirei o operador\n')

file.seek(0)
print(file.read())
file.close()

