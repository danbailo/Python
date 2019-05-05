#manipulacao de linha de comando
#https://docs.python.org/3/library/argparse.html

import sys

def soma(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mult(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

if sys.argv[1] == "soma":
    print(soma(int(sys.argv[2]), int(sys.argv[3])))
if sys.argv[1] == "sub":
    print(sub(int(sys.argv[2]), int(sys.argv[3])))
if sys.argv[1] == "mult":
    print(mult(int(sys.argv[2]), int(sys.argv[3])))
if sys.argv[1] == "div":
    print(div(int(sys.argv[2]), int(sys.argv[3])))
