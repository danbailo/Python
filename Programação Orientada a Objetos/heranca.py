#self = objeto
#cls = classe

class Funcionario:
	aumento = 1.04

	def __init__(self, nome, salario):
		self.nome = nome
		self.salario = salario
	
	def dados(self): #getter
		return {"nome": self.nome, "salario": self.salario}

	def aplicar_aumento(self):
		self.salario *= self.aumento

	@classmethod #manipula atributos da classe, e nao do obj
	def definir_novo_aumento(cls, novo_aumento):
		cls.aumento = novo_aumento

	@staticmethod #n exige nenhum argumento da classe/ n precisa instanciar um obj
	def dia_util(dia):
		if dia.weekday() in [5,6]:
			return False
		return True

	def __repr__(self):
		return "Nome: " + self.dados()["nome"] + ", salário: " + str(self.dados()["salario"])

class Admin(Funcionario):
	def __init__(self, nome, salario):
		super().__init__(nome, salario)
	
	def atualizar_dados(self, salario): #setter
		self.salario = salario
		# return self.dados()

func1 = Funcionario("daniel", 1000)
func2 = Funcionario("josue", 3250)

print(func1.dados())
print(func2.dados())

admin1 = Admin("naul", 5000)

print(admin1.dados())

admin1.atualizar_dados(7632)

print(admin1.dados())

print(admin1)

#aplicando aumento
print("\naplicando aumento\n")
func1.aplicar_aumento()
print(func1)

#modificando atributo da classe
func1 = Funcionario("daniel", 1000)
print("\naplicando novo aumento\n")
Funcionario.definir_novo_aumento(1.05)
func1.aplicar_aumento()
print(func1)

import datetime

minha_data = datetime.date(2020, 5, 16)

print(Funcionario.dia_util(minha_data))