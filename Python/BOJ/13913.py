# 숨바꼭질 4
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,k = map(int,input().split())
MAX_INDEX = 100000
dist = [MAX_INDEX] * (MAX_INDEX+1)
board = [0] * (MAX_INDEX+1)
q = deque()
q.append(n)
dist[n] = 0
while q:
    x = q.popleft()
    if x == k:
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= MAX_INDEX and dist[nx] == MAX_INDEX:
            dist[nx] = dist[x] + 1
            board[nx] = x
            q.append(nx)

def move(n,m):
    if n != m:
        move(n,board[m])
    print(m,end=' ')

print(board[k])
move(n,k)