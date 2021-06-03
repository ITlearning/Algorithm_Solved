# 정확한 순위
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
board = [[INF] * (n+1) for _ in range(n+1)]
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            board[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    board[a][b] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])
result = 0
for a in range(1,n+1):
    cnt = 0
    for b in range(1,n+1):
        if board[a][b] != INF or board[b][a] != INF :
            cnt += 1
    if cnt == n:
        result += 1

print(result)