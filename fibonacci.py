def fib(n):
    dp=[]
    dp=[-1 for i in range(n+2)]
    if (n==0 or n==1):
        return n
    if (dp[n]!=-1):
        return dp[n]
    dp[n]=fib(n-1)+fib(n-2) #recursive
    return dp[n]

def fib2(n):
    if n==0 or n==1:
        return n
    dp=[-1 for i in range(n+2)]
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

print(fib(6))
print(fib2(6))
