import re
class ExtratorURL:
    def __init__(self, url): #iniciando a classe
        self.url = self.sanitiza_url(url)
        self.valida_url(self.url)

    def sanitiza_url(self, url):#limpando a string(tiando espaços e caracteres epeciais)
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self, url):#validando a url
        if not self.url:
            raise ValueError("A URL esta vazia!!")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")# o minimo que a url deve ter

        match = padrao_url.match(url)

        if not match:
            raise ValueError("A URl NÃO É VALIDA")


    def get_url_base(self, url):#pegando a base da url
        url_busca = self.url.find("?")#pesquisa na url
        url_base = url[:url_busca]
        return url_base

    def get_url_parametros(self, url):#pegando os parametros da url
        url_busca = self.url.find("?")#pesquisa na url
        url_parametros = self.url[url_busca + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)#achando a localização do parametro passado
        indice_valor = indice_parametro + len(parametro_busca) + 1 #pegando o parametro interio somando a localização a ele mesmo 
        indice_e_comercial = self.get_url_parametros().find("=", indice_valor)#ahcando outro parametro a partir da posção do anterior
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"\nURL: {self.url} \nParametros: {self.get_url_parametros(self.url)} \nBase da URL: {self.get_url_base(self.url)}" 
                
    def __eq__(self, other):
        return self.url == other

url = "https://www.bytebank.com.br/cambio?q=macarr%C3%A3o&rs=typed&term_meta,[]=macarrao=%C3%A3o%7Ctyped"
# print(len(url))


extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
# # extrator_url = ExtratorURL(None)

print(extrator_url == extrator_url2)

print("Tamanho da URL: ",len(extrator_url))
print(extrator_url)

# valor_quantidade = extrator_url.get_valor_parametro("macarr")
# print(valor_quantidade)