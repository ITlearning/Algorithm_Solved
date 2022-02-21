# 보물섬
from collections import deque

dx = [0,-1,0,1]
dy = [-1,0,1,0]

n,m = map(int,input().split())
board = []

deque_l = deque()
cnt = 0
for i in range(n):
    tmp = list(input())
    board.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == "L":
            deque_l.append([i,j])

def bfs(x,y):
    q = deque()
    q.append([x,y])
    distance = [[-1]*m for _ in range(n)]
    distance[x][y] = 0
    result = 0
    while q:
        x,y = q.popleft()
        for cur in range(4):
            nx = x + dx[cur]
            ny = y + dy[cur]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == "L" and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    result = max(result, distance[nx][ny])
                    q.append([nx,ny])
    
    return result


while deque_l:
    x,y = deque_l.popleft()
    cnt = max(cnt, bfs(x,y))
    
print(cnt)

