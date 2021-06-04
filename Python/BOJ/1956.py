# 운동
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
board = [[INF] * (n+1) for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int,input().split())
    board[a][b] = c

for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])
mini = INF
for a in range(1,n+1):
    mini = min(mini, board[a][a])
    

if mini == INF:
    print(-1)
else:
    print(mini)
