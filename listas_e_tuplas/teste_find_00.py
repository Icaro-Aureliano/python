import requests 
from bs4 import BeautifulSoup
import re

requisicao = requests.get("https://www.garca.sp.gov.br/portal/noticias/")


conteudo_requisicao = requisicao.content

pagina = BeautifulSoup(conteudo_requisicao, "html.parser")

# print(type(pagina))




busca_noticia = pagina.find("div", attrs={"class":"ntc_area_info_noticia"})

busca_titulo = busca_noticia.find("div", attrs={"class":"ntc_titulo_noticia sw_lato_black"})

titulo_noticia = busca_titulo.text

categoria = pagina.find("div", attrs={"class":"ntc_categoria_noticia sw_lato"})

categoria_noticia = categoria.text

print(titulo_noticia)
print(categoria_noticia)





# content_titulo = re.compile("[alt='][?][']")
# busca = content_titulo(titulo.text)


# print(busca)