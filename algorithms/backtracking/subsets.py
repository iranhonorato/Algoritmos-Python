from typing import List

def subsets(nums:List[int]) -> List[List[int]]:
    result = []
    tam = len(nums)
    sub = []

    def dfs(idx):
        if idx == tam:
            result.append(sub.copy())
            return 
        
        sub.append(nums[idx])
        dfs(idx+1)
        sub.pop()
        dfs(idx+1)

        return  
    

    dfs(0)
    return result


lista = [1,2,3]

print(subsets(lista))


