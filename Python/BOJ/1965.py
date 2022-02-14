# 상자넣기

n = int(input())

board = list(map(int,input().split()))

dp = [1 for _ in range(n+1)]

for i in range(1,n):
    for j in range(i):
        if board[i] > board[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

