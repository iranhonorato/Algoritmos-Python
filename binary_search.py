def binary_search(elemento:int, lista:list) -> int: 
    min_index = 0 
    max_index = len(lista) - 1 
    middle = int((min_index + max_index)/2)
    if elemento in lista:
        while lista[middle] != elemento:
            if lista[middle] < elemento:
                min_index = middle + 1

            if lista[middle] > elemento:   
                max_index = middle - 1

            middle = int((min_index + max_index)/2)
        if lista[middle - 1] == elemento:
            middle = binary_search(elemento, lista[:middle])

        return middle
        
    else: 
        return "Esse elemento não existe na lista"

    




lista = [0,0,0,0,0,1,1,1,1,1]
print(binary_search(1, lista))


