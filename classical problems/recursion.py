def fibonacci(n):
    if n <= 2:
        return 1 
    
    result = fibonacci(n-1) + fibonacci(n-2)
    return result




def fatorial(n):
    if n == 0:
        return 1
    
    result = n*fatorial(n-1)
    return result 


