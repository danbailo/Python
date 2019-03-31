class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def getNome(self):
		return self.nome
	
class Funcionario(Pessoa):
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def getNome(self):
		return self.nome

p = Pessoa('Daniel',19)

f = Funcionario('Naul',51)

print(p.getNome())
print(f.getNome())