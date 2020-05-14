import functools

def meu_decorador(funcao):
	@functools.wraps(funcao)
	def func_que_roda_funcao():
		print("************* Embrulhando funcao no decorador ************")
		funcao()
		print("************* Fechando embrulho! ************")
	return func_que_roda_funcao

@meu_decorador
def minha_funcao(): #decorador pega essa funcao como parametro de entrada
	print("Eu sou uma funcao :)")

minha_funcao() 