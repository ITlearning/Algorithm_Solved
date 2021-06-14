# 섬의 개수
# 상, 하 , 좌 , 우, 좌상, 좌하, 우상, 우하
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]
while True:
    board = []
    dist = []
    queue = deque()
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    
    for i in range(h):
        number = list(map(int,input().split()))
        board.append(number)
        dist.append([0] * (len(number)))

    for a in range(h-1):
        for b in range(w-1):
            if board[a][b] == 0:
                dist[a][b] = 1    
    cnt = 0
    for a in range(h):
        for b in range(w):
            if board[a][b] == 0: continue
            if dist[a][b] == 1: continue
            cnt += 1
            queue.append((a,b))
            dist[a][b] = 1
            while queue:
                x,y = queue.popleft()
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= h or ny < 0 or ny >= w : continue
                    if board[nx][ny] == 0 or dist[nx][ny] == 1 : continue
                    dist[nx][ny] = 1
                    queue.append((nx,ny))
    print(cnt)