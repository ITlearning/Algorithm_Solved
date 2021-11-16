# 음식물 피하기
import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())

board = [[0 for _ in range(m)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(k):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1

answer = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            continue
        q = deque()
        q.append([i,j])
        board[i][j] = 2
        cnt = 1
        while q:
            x,y = q.popleft()
            for cur in range(4):
                nx = x + dx[cur]
                ny = y + dy[cur]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0 or board[nx][ny] == 2:
                        continue
                    board[nx][ny] = 2
                    q.append([nx,ny])
                    cnt += 1
                
        answer = max(answer, cnt)
print(answer)
