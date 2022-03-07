# 타일링

import sys
input = sys.stdin.readline

# N 번째 직사각형을 채우는 방법으론
# 1. n-1 번째 직사각형에서 2x1 타일을 구하는 방법
# 2. n-2 번째 직사각형에서 2x2 타일을 구하는 방법
# 3. n-2 번째 직사각형에서 2x1 가로 타일을 구하는 방법
# 이 존재한다.

def problem(n):
    dp = [1,1,3]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2]*2) 
    
    return dp[n]


while True:
    n = input().rstrip()
    if n.isdigit():
        print(problem(n))
    else:
        break