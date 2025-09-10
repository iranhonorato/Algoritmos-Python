def fatorial(num:int) -> int:
    if num == 0:
        return 1 
    
    result = num*fatorial(num-1)
    return result 
