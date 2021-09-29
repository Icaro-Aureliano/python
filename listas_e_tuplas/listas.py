lista_idades = []
idade1 = 30
idade2 = 45
idade3 = 50

idades = [idade1, idade2, idade3]

lista_teste = [(idade**2) for idade in idades]

for idade in idades:
    lista_for = lista_idades.append(lista_teste*2)


lista_idades.extend(lista_teste)
print("\n\nLista for:", lista_for)
print("\n\nLista teste: ", lista_teste)
print("\n\nLista idades: ",lista_idades)
# print(lista_idades.index(45))





