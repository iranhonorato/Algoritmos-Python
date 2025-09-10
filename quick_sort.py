def particiona(inicio:int, lista:list, fim:int):
    lp = inicio
    pivo = lista[inicio]
    count = inicio + 1
    while count < fim:
        if lista[count] < pivo:
            lp += 1 
            lista[lp], lista[count] = lista[count], lista[lp]
        count += 1

    lista[lp], lista[inicio] = lista[inicio], lista[lp]
    return lista

# 

lista = [5,1,7,2,3,6,4]
print(particiona(0, lista, len(lista)))