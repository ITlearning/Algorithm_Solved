# 달리기
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())

dist = [[float('inf')]* (M) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
board = []
for i in range(N):
    text = list(input().rstrip())
    board.append(list(text))
x1,y1,x2,y2 = map(int,input().split())
q = deque()
c = 1
q.append((x1-1,y1-1))
dist[x1-1][y1-1] = 0

while q:
    x,y= q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        cnt = 1
        while cnt <= K and 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '#' and dist[nx][ny] > dist[x][y]:
            if dist[nx][ny] == float('inf'):
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1
            nx += dx[i]
            ny += dy[i]
            cnt += 1

if dist[x2-1][y2-1] == float('inf'):
    print(-1)
else:
    print(dist[x2-1][y2-1])
            
