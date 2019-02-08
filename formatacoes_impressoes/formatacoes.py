s = 'STRING'
print('Place another string with a mod and s: %s' %(s))

print('Floating point numbers: %1.3f' %(1354.154144))
print('Floating point numbers: %1.0f' %(13.144))
print('Floating point numbers: %1.5f' %(13.144))
print('Floating point numbers: %10.2f' %(13.144))

print('Here is a number: %s. Here is a string: %s' %(123.1,'hi'))
print('Here is a number: %r. Here is a string: %r' %(123.1,'hi'))

print('First: %s, Second: %1.2f, Third: %r' %('hi!',3.14,22))

#Usando o método string.format () -> melhor forma

print('String aqui {var1} e também {var2}'.format(var1 = 'something1', var2 = 'something2'))

print('teste {},{},{}'.format('anything','2','3'))

print('One:{a}, Two:{b}, Three:{c}'.format(a=1,b='two',c=12.3))