def bubble_sort(lista:list) -> list:
    troca = True
    while troca:
        troca = False 
        for i in range(len(lista) - 1):
            if lista[i+1] < lista[i]:
                troca = True 
                lista[i+1], lista[i] = lista[i], lista[i+1]
    return lista
