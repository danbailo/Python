# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:05:12 2019

@author: ecorrea
"""

#P053 SELECT *
import sqlite3

#(1)-Conecta com o BD
nomeBD = 'C:/CursoPython/RH.db'
minha_conn = sqlite3.connect(nomeBD)

#(2)-Executa o SQL
c = minha_conn.cursor()
c.execute('SELECT * FROM Funcionario')

#(3)-Exibe os resultados

#(3.1)-Obtém e exibe os nomes das colunas
nomes_colunas = next(zip(*c.description)) 
print(nomes_colunas) 

#(3.2)-Obtém e exibe cada linha recuperada do BD
for linha in c:
    print(linha)

#(4)-Fecha a conexão
minha_conn.close()

