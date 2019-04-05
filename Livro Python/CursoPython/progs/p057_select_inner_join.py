# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:25:42 2019

@author: ecorrea
"""

#P057 SELECT com INNER JOIN
import sqlite3

#(1)-Conecta com o BD
nomeBD = 'C:/CursoPython/RH.db'
minha_conn = sqlite3.connect(nomeBD)

#(2)-Monta e Executa o SQL
c = minha_conn.cursor()

vSQL = """SELECT F.*, P.*
     FROM Funcionario F INNER JOIN Profissao P 
     ON (F.id_prof = P.id) 
     """ 

c.execute(vSQL)

#(3)-Exibe os resultados

#(3.1)-Obtém e exibe os nomes das colunas
nomes_colunas = next(zip(*c.description)) 
print(nomes_colunas) 

#(3.2)-Obtém e exibe cada linha recuperada do BD
for linha in c:
    print(linha)

#(4)-Fecha a conexão
minha_conn.close()
