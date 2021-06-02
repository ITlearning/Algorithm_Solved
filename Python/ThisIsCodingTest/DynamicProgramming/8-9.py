# 병사 배치하기

# 가장 긴 증가하는 부분 수열(LIS)

n = int(input())
board = list(map(int, input().split()))
board.reverse()

dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if board[j] < board[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))