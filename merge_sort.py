

def merge(left:list, right:list, array:list) -> list:

    i = 0
    j = 0 
    k = 0
    while k < len(array):
        if i == len(left):
            array[k] = right[j]
            j +=1 
        elif j == len(right):
            array[k] = left[i]
            i += 1 
        elif left[i] > right[j]:
            array[k] = right[j]
            j += 1 
        else:
            array[k] = left[i]
            i += 1
        k += 1
    return array




def merge_sort(array:list) -> None:
    if len(array) <= 1:
        return 
    
    meio = int(len(array)/2)
    left = [-1 for i in range(meio)]
    right = [-1 for j in range(len(array) - meio)]
    for i in range(len(array)):
        if i < meio:
            left[i] = array[i]
        else: 
            right[i - meio] = array[i]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, array)


lista = [2,4,3,1,5]
merge_sort(lista)
print(lista)


