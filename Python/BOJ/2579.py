# 계단 오르기
n = int(input())
board = [0 for _ in range(n+3)]
for i in range(1,n+1):
    board[i] = int(input())

dp = [0 for _ in range(n+3)]

dp[1] = board[1]
dp[2] = board[1] + board[2]
dp[3] = max(board[1] + board[3],board[2] + board[3])

for i in range(4,n+1):
    dp[i] = max(dp[i-3] + board[i-1] + board[i], dp[i-2] + board[i])

print(dp[n])