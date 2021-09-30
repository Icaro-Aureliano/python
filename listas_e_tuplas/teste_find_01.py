import requests 
from bs4 import BeautifulSoup
import re

requisicao = requests.get("https://www.garca.sp.gov.br/portal/noticias/")


conteudo_requisicao = requisicao.content

pagina = BeautifulSoup(conteudo_requisicao, "html.parser")

# print(type(pagina))

noticias = pagina.findAll("div", attrs={"class":"ntc_noticia"})

for noticia in noticias:

    busca_noticia = noticia.find("div", attrs={"class":"ntc_area_info_noticia"})

    titulo = noticia.find("div", attrs={"class":"ntc_titulo_noticia sw_lato_black"})

    categoria = noticia.find("div", attrs={"class":"ntc_categoria_noticia sw_lato"})

    texto_titulo = titulo.text
    texto_categoria = categoria.text
    
    print(f"Titulo: {texto_titulo} -- {texto_categoria} \n")

# content_titulo = re.compile("[alt='][?][']")
# busca = content_titulo(titulo.text)


# print(busca)