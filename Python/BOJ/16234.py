# 인구 이동
from collections import deque
n,l,r = map(int,input().split())

dx = [0,-1,0,1]
dy = [-1,0,1,0]
board = []

for i in range(n):
    board.append(list(map(int,input().split())))

def bfs(i,j):
    dist[i][j] = 1
    q = deque()
    q.append([i,j])
    tmp = []
    tmp.append([i,j])
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 0:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    dist[nx][ny] = 1
                    q.append([nx,ny])
                    tmp.append([nx,ny])
    return tmp

cnt = 0
while True:
    dist = [[0 for _ in range(n)] for _ in range(n)]
    t = False
    for i in range(n):
        for j in range(n):
            if dist[i][j] == 0:
                result = bfs(i,j)
                if len(result) > 1:
                    t = True
                    num = sum(board[x][y] for x,y in result) // len(result)
                    for x,y in result:
                        board[x][y] = num
    if t == False:
        break
    cnt += 1

print(cnt)