t = int(input())

def DP(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else: 
        return DP(n-1) + DP(n-2) + DP(n-3)

for i in range(t):
    n = int(input())
    
    print(DP(n))

# 점화식 : answer = dp(n-1) + dp(n-2) + dp(n-3)
# 하,, 점화식 큰일이다.