# 벽 부수고 이동하기
import sys
from collections import deque
n,m = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = []
for _ in range(n):
    num = list(map(int,list(input().rstrip())))
    board.append(list(num))

def dfs():
    q = deque()
    q.append([0,0,1])
    dist = [[[0]*2 for i in range(m)]for i in range(n)]
    dist[0][0][1] = 1
    while q:
        a,b,w = q.popleft()
        if a == n-1 and b == m-1:
            return dist[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                # 벽이고 벽을 뚫을 수 있는 상태이면
                if board[x][y] == 1 and w == 1:
                    dist[x][y][0] = dist[a][b][1] + 1
                    q.append([x,y,0])
                elif board[x][y] == 0 and dist[x][y][w] == 0:
                    dist[x][y][w] = dist[a][b][w] + 1
                    q.append([x,y,w])
    return -1
            

print(dfs())
