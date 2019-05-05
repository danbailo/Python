a = 1
b = 2
c = 3

if True:
    print("hello world")
elif True: #ja entrou no if, logo n entra aq
    print("sad")

if a>b:
    print("nao vai entrar aqui")
elif c>b:
    print("c é maior")
else:
    print("anything")

d={"Daniel":10,"Josué":7,"Lucas":2}
j = "Lucas" #Nome do aluno

if d[j] >= 9:
    print("Aprovado!")
elif d[j] >= 7:
    print("Recuperação!")
else:
    print("Reprovado!")