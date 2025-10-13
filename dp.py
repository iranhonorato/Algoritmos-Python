def finbonacci_dp(n, memo=None):
    if memo == None: 
        memo = [-1 for i in range(n)]

    if n < 2 or n == 2:
        memo[n-1] = 1 
        return memo[n-1]
    
    if memo[n-1] == -1:
        memo[n-1] = finbonacci_dp(n-1, memo) + finbonacci_dp(n-2, memo)
        return memo[n-1]
    
    else:
        return memo[n-1]
        

print(finbonacci_dp(100))
