l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]

print(l1 == l2)

print(l1 is l2)

print(id(l1))
print(id(l2))

l1.

#São duas listas diferentes, com referências diferentes à memória mas com valores iguais.
#O operador igual, compara somente o conteudo, o "is", verifica todos os aspectos, logo
# so retona true, se o objeto for realmente este

#https://pt.stackoverflow.com/questions/38104/em-python-quais-as-consequ%C3%AAncias-em-usar-is-no-lugar-de