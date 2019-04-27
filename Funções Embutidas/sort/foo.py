import operator

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def getName(self):
		return self.name

	def getAge(self):
		return self.age

p1 = Person('Lucas',23)
p3 = Person('Naul',51)
p2 = Person('Daniel',19)
p4 = Person('Josué',19)
p5 = Person('Lucilei',43)
p6 = Person('José',27)

people = [p1,p2,p3,p4,p5,p6]

people.sort(key=operator.attrgetter('age'), reverse=True)

for person in people:
	print(person.getName(),', %d years old' % (person.getAge()))