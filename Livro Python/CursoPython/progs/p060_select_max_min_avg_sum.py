# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:05:11 2019

@author: ecorrea
"""

#P060 SELECT com MAX, MIN, AVG, SUM
import sqlite3

#(1)-Conecta com o BD
nomeBD = 'C:/CursoPython/Reformas.db'
minha_conn = sqlite3.connect(nomeBD)

#(2)-Executa o SQL e exibe os resultados
c = minha_conn.cursor()
vSQL = "SELECT MIN(custo), MAX(custo), AVG(custo), SUM(custo) FROM Projeto" 
c.execute(vSQL)
for linha in c:
    print(linha)

#(3)-Fecha a conexão
minha_conn.close()