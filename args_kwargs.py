def poucos_args(arg1, arg2):
	return arg1 + arg2

def muitos_args(arg1, arg2, arg3, arg4, arg5):
	return arg1 + arg2 + arg3 + arg4 + arg5

print(poucos_args(1,2)) 
print(muitos_args(1,2,3,4,5))

#solucao 1
def utilizando_lista(lista):
	return sum(lista)

print(utilizando_lista([1,2,3,4,5,32,1,2]))

#utilizando args
def utilizando_args(*args): # posso passar a qqr qtd
	return sum(args)

print(utilizando_args(1,2,3,4,5,6,7,8,9,0,10,2,3,12))

#utilizando args e kwargs

def my_args(*args, **kwargs):
	print(args)
	print(kwargs)

my_args("daniel", 20, "oii", "args", nome="Daniel", idade=20)