# 탈출
from collections import deque
r,c = map(int,input().split())

q = deque()
board = []

dist = [[0 for _ in range(c)] for _ in range(r)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

class beaver_home:
    x = 0
    y = 0

for i in range(r):
    tmp = list(input())
    board.append(tmp)

for i in range(r):
    for j in range(c):
        if board[i][j] == 'D':
            beaver_home.x = i
            beaver_home.y = j
        if board[i][j] == 'S':
            q.append([i,j])
            
for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            q.append([i,j])

flag = False
# 불 먼저
while q:
    x,y = q.popleft()

    if board[beaver_home.x][beaver_home.y] == 'S':
        flag = True
        break

    for cur in range(4):
        nx = x + dx[cur]
        ny = y + dy[cur]
        if 0 <= nx < r and 0 <= ny < c:
            if (board[nx][ny] == '.' or board[nx][ny] == 'D') and board[x][y] == 'S':
                board[nx][ny] = 'S'
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])
            elif (board[nx][ny] == '.' or board[nx][ny] == 'S') and board[x][y] == '*':
                board[nx][ny] = '*'
                q.append([nx,ny])

if flag:
    print(dist[beaver_home.x][beaver_home.y])
else:
    print("KAKTUS")