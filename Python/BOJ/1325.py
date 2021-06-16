# 효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 1
    while q:
        d = q.popleft()
        for n in board[d]:
            if check[n] == 0:
                check[n] = 1
                q.append(n)

n,m = map(int,input().split())
board = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    board[b].append(a)
res = []
print(board)
for i in range(1,n+1):
    check = [0] * (n+1)
    bfs(i)
    res.append(check.count(1))

big = max(res)
for i in range(n):
    if res[i] == big:
        print(i+1, end=' ')
print()