def selection_sort(lista:list) -> list:
    for i in range(len(lista)):
        min_index = i 

        for j in range(min_index+1, len(lista)):
            if lista[j] < lista[min_index]:
                lista[j], lista[min_index] = lista[min_index], lista[j]

    return lista
lista = [5,1,7,2,3,6,4]
print(selection_sort(lista))
