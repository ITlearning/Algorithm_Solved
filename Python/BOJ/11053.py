# 가장 긴 증강하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
board = []
board.append(list(map(int,input().split())))
dp = [1] * (n)
dp[0] = 1
for j in range(1,n):
    for i in range(j):
        if board[0][i] < board[0][j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))