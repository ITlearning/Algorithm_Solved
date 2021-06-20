# 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
MAX_INDEX = 100000
board = [-1] * (MAX_INDEX+1)
dist = [False] * (MAX_INDEX+1)
q = deque()
q.append(n)
board[n] = 0
#dist[n] = True
while q:
    x = q.popleft()
    if x == k:
        break
    if x * 2 <= MAX_INDEX and board[x*2] == -1: #dist[x*2] == False:
        q.append(x*2)
        board[x*2] = board[x]
        #dist[x*2] = True
    
    for nx in (x-1, x+1):
        if 0 <= nx <= MAX_INDEX and board[nx] == -1: #dist[nx] == False:
            q.append(nx)
            board[nx] = board[x] + 1
            #dist[nx] = True
print(board[k])