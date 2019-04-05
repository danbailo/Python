import sys

class HashTable:

	def __init__(self, table_size):

		if table_size < 1:
			print('Erro: o tamanho da tabela tem que ser positivo!')
			sys.exit(1)

		self.table_size = table_size
		self.table = [[] for i in range(table_size)]

	def hash_func(self, key):
		return key % self.table_size

	def insert(self, key):
		self.table[self.hash_func(key)].append(key)

	def show(self):

		for linked_list in self.table:
			if linked_list:
				for key in linked_list:
					print('%d' % key, end = ' ')
				print('')

	def search(self, key):
		if key in self.table[self.hash_func(key)]:
			return True
		return False

def prime_number(n):
    prime = 0
    for i in range(n):
        if n%(i+1)==0:
            prime += 1
    if prime == 2:
        return True
    return False

print(prime_number(11))

# d = HashTable(9) #mais colisoes
d = HashTable(11) #if tam == prime number, collision number is lower

d.insert(19)
d.insert(28)
d.insert(20)
d.insert(5)
d.insert(33)
d.insert(15)

d.show()