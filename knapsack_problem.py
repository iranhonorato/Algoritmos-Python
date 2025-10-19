def knapsack_solution(weights:list, values:list, capacity:int, idx=0, current_value=0, current_choices=None, best=None):
    n = len(weights)

    if current_choices == None: 
        current_choices = [False for i in range(n)]
    if best == None:
        best = {"value": 0, "choices":[False for i in range(n)]}
    

    if idx == n or capacity <= 0:
        if current_value > best["value"]:
            best["value"] = current_value
            choices = current_choices.copy()
            best["choices"] = choices
        return best 
    
    # 1º caso: Não seleciona nenhum objeto 
    current_choices[idx] = False 
    knapsack_solution(weights, values, capacity, idx+1, current_value, current_choices, best)


    #2º caso: Seleciona um objeto  
    if weights[idx] <= capacity:  # verifica se o objeto cabe na mochila
        current_choices[idx] = True  # se couber, põe True no idx equivalente ao idx do objeto
        current_value += values[idx] # idem, adiciona o valor do objeto ao valor atual 
        knapsack_solution(weights, values, capacity-weights[idx], idx+1, current_value, current_choices, best)

    return best


weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50


result = knapsack_solution(weights, values, capacity)
print(result)