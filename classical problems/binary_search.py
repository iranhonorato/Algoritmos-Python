def binary_search(elemento:int, lista:list) -> int: 
    min_index = 0 
    max_index = len(lista) - 1 
    count = 0 
    while min_index <= max_index:
        middle = int((min_index + max_index)/2)

        if lista[middle] == elemento:
            return f"Elemento encontrado após {count} iterações no índice {middle}"
        
        elif lista[middle] < elemento:
            min_index = middle + 1
        
        else:
            max_index = middle - 1

        
        count += 1

    return f"O elemento em questão não está no array"
    




lista = [i for i in range(100)]
print(binary_search(5, lista))


