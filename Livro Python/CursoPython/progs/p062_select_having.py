# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:08:26 2019

@author: ecorrea
"""

#P062 SELECT com GROUP BY e HAVING
import sqlite3

#(1)-Conecta com o BD
nomeBD = 'C:/CursoPython/Reformas.db'
minha_conn = sqlite3.connect(nomeBD)

#(2)-Executa o SQL e exibe os resultados
c = minha_conn.cursor()
vSQL = """
	 SELECT 
          tipo,
          local,
          SUM(custo) 
       FROM Projeto
       GROUP BY tipo, local
       HAVING SUM(custo) >= 600000
       """ 
 
c.execute(vSQL)
for linha in c:
    print(linha)

#(3)-Fecha a conexão
minha_conn.close()