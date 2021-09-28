url = "https://br.pinterest.com/search/pins/?q=macarr%C3%A3o&rs=typed&term_meta[]=macarrao=%C3%A3o%7Ctyped"#passando a url
# url = "        "

# url = url.replace(" ", "") # tirando espaçamentos e caracteres especiais das strings
url = url.strip()


if url == "":
    raise ValueError("A URL esta vazia!!")

print("\n")


url_busca = url.find("?")#pesquisa na url
url_base = url[:url_busca]#usando a pesquisa como base de localização
url_parametros = url[url_busca+1:]
print(url_base)
print(url_parametros)


#Busca valor de um parametro
parametro_busca = "macarr"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)