# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:53:01 2019

@author: notebook
"""

#P042 – Gravando um arquivo texto
fout = open('C:/CursoPython/toque_fragil.txt', 'w')
msg1 = "O sorriso\n"
msg2 = "Do\n"
msg3 = "Cachorro\n"
msg4 = "Tá\n"
msg5 = "No rabo...\n"

fout.write("Toque Frágil (Walter Franco)\n")
fout.write("============ ===============")
fout.write("\n")
fout.write(msg1 + msg2 + msg3 + msg4 + msg5)
fout.close()
