# 플로이드 - 워셜 알고리즘

from sys import stdin
from math import inf

n = int(stdin.readline())
m = int(stdin.readline())

board = [[inf] * n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, stdin.readline().split())
    board[a-1][b-1] = min(board[a-1][b-1], c)

for k in range(n):
    board[k][k] = 0
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for row in board:
    for i in range(n):
        if row[i] == inf:
            row[i] = 0
        print(row[i], end=" ")
    print()
