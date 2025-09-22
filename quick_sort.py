def particiona(lista:list, inicio:int, fim:int) -> int:
    lp = inicio
    pivo = lista[inicio]
    count = inicio + 1
    while count < fim:
        if lista[count] < pivo:
            lp += 1 
            lista[lp], lista[count] = lista[count], lista[lp]
        count += 1

    lista[lp], lista[inicio] = lista[inicio], lista[lp]
    return lp




def quick_sort(lista:list, inicio:int, fim:int):
    if inicio < fim:
        lp = particiona(lista, inicio, fim)
        quick_sort(lista, inicio, lp)
        quick_sort(lista, lp+1, fim)
    return lista


lista = [5,1,7,2,3,6,4]
print(quick_sort(lista,0,len(lista)))


