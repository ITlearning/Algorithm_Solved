# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

def bfs(n,k):
    q = deque()
    q.append((n))

    board = [0] * 100001

    while q:
        x = q.popleft()
        if x == k:
            return board[x]
        for i in (x-1,x+1, x*2):
            if 0 <= i < 100001 and board[i] == 0:
                board[i] = board[x]+1
                q.append(i)


print(bfs(n,k))