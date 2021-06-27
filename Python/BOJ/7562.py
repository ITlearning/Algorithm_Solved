# 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]
while t != 0:
    N = int(input())
    start_x,start_y = map(int,input().split())
    target_x, target_y = map(int,input().split())
    dist = [[0 for i in range(N)] for i in range(N)]
    dist[start_x][start_y] = 1
    q = deque()
    q.append((start_x,start_y))
    while q:
        x,y = q.popleft()
        if x == target_x and y == target_y:
            print(dist[x][y]-1)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if dist[nx][ny] >= 1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))
    t -= 1