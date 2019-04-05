# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 15:07:16 2019

@author: notebook
"""

#P093: Criando e Removendo Colunas em um DataFrame
#     (usando o Python padrão)
import pandas as pd  

#(1)-Define função para converter idade em FaixaEtária
def fx_etaria(idade):
    if (idade < 18) :
        return '<18'
    elif (idade >= 18 and idade < 30) :
        return '18-29'
    elif (idade >= 30 and idade < 40) :
        return '30-39'
    else :
        return '>=40'

#(2)-Importa CSV para o DataFrame
pessoas = pd.read_csv('C:/CursoPython/pessoas.csv')
print('* * DataFrame original:')           
print(pessoas)           
print('---------------------------------------')

#(3)-Cria uma lista com todas as faixa etárias
lst_faixa_etaria = []
for i in range(len(pessoas)):
    idade = pessoas.iloc[i]['idade'] #pega a idade da pessoa i
    faixa_etaria = fx_etaria(idade)  #obtém a faixa etária da pessoa i   
    lst_faixa_etaria.append(faixa_etaria)  #insere no fim da lista
    
print('* * Lista de faixa etárias:')           
print(lst_faixa_etaria)
print('---------------------------------------')

#(4)-Cria uma nova coluna no DataFrame, chamada "faixa_etaria"
pessoas['faixa_etaria'] = lst_faixa_etaria
print('* * DataFrame com a coluna "faixa_etaria" inserida:')           
print(pessoas)           
print('---------------------------------------')

#(5)-Remove a coluna idade
pessoas = pessoas.drop('idade', axis=1)
print('* * DataFrame com a coluna "idade" removida:')           
print(pessoas)           
print('---------------------------------------')
