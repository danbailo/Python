import pyqrcode
from pyqrcode import QRCode

#String que representa o qr code
s = "em python né papi kk, hj tem tempo pra ver uns snippets"

url = pyqrcode.create(s)

#cria e salva a svg file nomeado por "myqr.svg"

url.svg("myqr.svg", scale=8, background="white")