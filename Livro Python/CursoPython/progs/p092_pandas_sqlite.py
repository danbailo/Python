# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:25:11 2019

@author: notebook
"""

#P092 pandas x sqlite
import sqlite3
import pandas as pd

#(1)-Conecta com o BD
nomeBD = 'C:/CursoPython/RH.db'
minha_conn = sqlite3.connect(nomeBD)

#(2)-Executa comando SQL 
c = minha_conn.cursor()
c.execute('SELECT * FROM Funcionario')

#(2.1)-armazena todos os resultados em memória com o método fetchall()
linhas = c.fetchall()

#(2.2)-pega os nomes das colunas com a propriedade description
nomes_colunas = next(zip(*c.description))

#(3)-Transfere os dados obtidos para um DataFrame 
d=pd.DataFrame(linhas,columns=nomes_colunas)

print(d)

minha_conn.close()
