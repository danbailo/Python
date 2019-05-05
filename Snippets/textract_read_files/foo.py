#read doc/pdf file in python    
from textract import process

#retorna o conteudo em bytes
data = process("sample.doc")

#converte o conteudo em bytes para string
data = process("sample.doc").decode("utf-8")

print(data)