# 숨바꼭질 2
from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
MAX_SIZE = 100001
board = [[MAX_SIZE, 0] for _ in range(MAX_SIZE)]

q = deque()

q.append(n)
board[n][0] = 0
board[n][1] = 1

while q:
    x = q.popleft()
    for nx in [x-1, x+1, x*2]:
        if 0 <= nx < MAX_SIZE:
            if board[nx][0] == MAX_SIZE:
                q.append(nx)
                board[nx][0] = board[x][0] + 1
                board[nx][1] = board[x][1]
            elif board[nx][0] == board[x][0]+1:
                board[nx][1] += board[x][1]

print(board[k][0])
print(board[k][1])