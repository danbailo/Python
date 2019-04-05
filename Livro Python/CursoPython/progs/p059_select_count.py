# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:02:45 2019

@author: ecorrea
"""

#P059 SELECT com COUNT
import sqlite3

#(1)-Conecta com o BD
nomeBD = 'C:/CursoPython/Reformas.db'
minha_conn = sqlite3.connect(nomeBD)

#(2)-Executa o SQL e exibe os resultados
c = minha_conn.cursor()
vSQL = "SELECT COUNT(codigo), COUNT(custo), COUNT(*) FROM Projeto" 
c.execute(vSQL)

for linha in c:
    print(linha)

#(3)-Fecha a conexão
minha_conn.close()