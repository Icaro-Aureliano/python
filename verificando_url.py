'''URL validas:
bytebank.com/cambio
bytebank.com.br/cambio
https://www.bytebank.com.br/cambio
www.bytebank.com.br/cambio
www.bytebank.com/cambio

URL invalida:
https://bytebank/cambio
http://bytebank.naoexiste/cambio
ht:bytebank.naoexiste/cambio'''
import re


url = "https://www.bytebank.com.br/cambio"
padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")

match = padrao_url.match(url)

if not match:
    raise ValueError("A URl NÃO É VALIDA")

print("A URL É VALIDA!!")
