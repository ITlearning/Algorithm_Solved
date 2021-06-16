# 바닥 장식
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(input()))
cnt = 0
for i in range(n):
    tmp = ""
    for j in range(m):
        if board[i][j] == '-':
            if board[i][j] != tmp: cnt += 1
        tmp = board[i][j]

for j in range(m):
    tmp = ""
    for i in range(n):
        if board[i][j] == '|':
            if board[i][j] != tmp: cnt += 1
        tmp = board[i][j]

print(cnt)