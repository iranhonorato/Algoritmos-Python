

def merge(left:list, right:list) -> list:

    total_length = len(left) + len(right)
    result = [-1 for i in range(total_length)]

    i = 0
    j = 0 
    for k in range(total_length):
        if i == len(left):
            result[k] = right[j]
            j +=1 
        elif j == len(right):
            result[k] = left[i]
            i += 1 
        elif left[i] > right[j]:
            result[k] = right[j]
            j += 1 
        else:
            result[k] = left[i]
            i += 1
    return result




