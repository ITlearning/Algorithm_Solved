# 포도주 시식

n = int(input())

wine = [0 for _ in range(n+1)]

for i in range(1, n+1):
    wine[i] = int(input())

dp = [0 for _ in range(n+1)]

dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

#for i in range(3, n+1):
#   first = dp[]
print(dp)
print(max(dp))