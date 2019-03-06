#Datetime
#O Python possui o módulo de datetime para ajudar a lidar com timestamps em seu código. 
# Os valores de tempo são representados com a classe de time. Time têm atributos por hora, 
# minuto, segundo e microssegundo. Eles também podem incluir informações de fuso horário. 
# Os argumentos para inicializar uma instância de time são opcionais, mas é improvável que o 
# padrão de 0 seja o que você deseja.

#Time
#Vamos dar uma olhada em como podemos extrair informações de tempo do módulo datetime. 
# Podemos criar um timestamp especificando datetime.time(hour, minute, second, microsecond)

import datetime

t = datetime.time(4, 20, 1)
# Vamos mostrar as diferenças entre os componentes

print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

#Nota: Uma instância de tempo apenas mantém valores de tempo e não uma data associada ao tempo.

#Também podemos verificar os valores mínimos e máximos que uma hora do dia pode ter no módulo:
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)
#The min and max class attributes reflect the valid range of times in a single day.

#Dates
#O datetime (como você talvez tenha suspeitado) também nos permite trabalhar com timestamps
#  de data. Os valores da data do calendário são representados com a classe de data. 
# As instâncias possuem atributos por ano, mês e dia. É fácil criar uma data que represente a
#  data de hoje usando o método de classe today().

#Vamos ver alguns exemplos:
print('\n')
today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)

print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)

#Outra maneira de criar novas instâncias de data usa o método replace () de uma data existente.
# Por exemplo, você pode mudar o ano, deixando o dia e o mês sozinhos.

d1 = datetime.date(2015, 3, 11)
print('d1:', d1)

d2 = d1.replace(year=1990)
print('d2:', d2)

#Operações aritméticas
#Podemos realizar operações aritmética em objetos de data para verificar diferenças horárias. 
# Por exemplo:

print(d1)
print(d2)

print(d1-d2)

#Isso nos dá a diferença em dias entre as duas datas. Você pode usar o método timedelta para especificar várias unidades de horas (dia, minutos, horas, etc.)

#Ótimo! Agora você deve ter uma compreensão básica sobre como usar o Datetime com o Python para trabalhar com timestamps em seu código!

print(type(d1))

str_date = d1.strftime('%Y-%m-%d')
print(type(str_date))

print(str_date)
print(str_date.split('-'))
print(str_date.split(' '))
