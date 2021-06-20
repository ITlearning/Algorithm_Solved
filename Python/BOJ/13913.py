# 숨바꼭질 4
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,k = map(int,input().split())
MAX_INDEX = 100000
board = [MAX_INDEX] * (MAX_INDEX+1)
move_to = [0] * (MAX_INDEX + 1)
q = deque()
q.append(n)
board[n] = 0
while q:
    x = q.popleft()
    if x == k:
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= MAX_INDEX and board[nx] == MAX_INDEX:
            q.append(nx)
            board[nx] = board[x] + 1
            move_to[nx] = x

def move(n,m):
    if n != m:
        move(n,move_to[m])
    print(m, end=' ')

print(board[k])
move(n,k)