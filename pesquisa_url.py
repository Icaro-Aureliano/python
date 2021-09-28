url = "https://br.pinterest.com/search/pins/?q=macarr%C3%A3o&rs=typed&term_meta[]=macarrao=%C3%A3o%7Ctyped"#passando a url
print("\n")

url_busca = url.find("?")#pesquisa na url

url_base = url[:url_busca]#usando a pesquisa como base de localização

url_parametros = url[url_busca+1:]

print(url_parametros)

parametro_busca = "macarrao"
indice_parametro = url_parametros.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1

teste_indice = url_parametros[indice_valor:]

print(teste_indice)