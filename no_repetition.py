A = [1,2,1,1,2,3,1]
res = [None, None, None]

ultimo_indice = 0
for i in range(len(A)):
    achou = False
    for j in range(len(res)):
        if res[j] == A[i]:
            achou = True
            break
    if achou == False:
        res[ultimo_indice] = A[i]
        ultimo_indice += 1 
    
