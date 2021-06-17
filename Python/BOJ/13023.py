# ABCDE
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

board = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    board[a].append(b)
    board[b].append(a)

dist = [False for _ in range(n)]

def dfs(v, cnt):
    global t
    dist[v] = True
    if cnt >= 4:
        t = True
        return
    for a in board[v]:
        if not dist[a]:
            dfs(a, cnt+1)
            dist[a] = False

t = False

for i in range(n):
    dfs(i,0)
    dist[i] = False
    if t:
        break

print(1 if t else 0)

# https://hjp845.tistory.com/89 