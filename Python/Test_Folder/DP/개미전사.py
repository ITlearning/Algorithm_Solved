N = int(input())

board = list(map(int,input().split()))

dp = [0] * 100

dp[0] = board[0]
dp[1] = max(board[0], board[1])

for i in range(2,N):
    dp[i] = max(dp[i-1], dp[i-2]+board[i])

print(dp[N-1])