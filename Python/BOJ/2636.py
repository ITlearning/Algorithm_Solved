# 치즈
from collections import deque
n,m = map(int,input().split())
dx = [0,-1,0,1]
dy = [-1,0,1,0]
board = []

for i in range(n):
    board.append(list(map(int,input().split())))
cnt = 0
one = 0
while True:
    dist = [[0 for _ in range(m)] for _ in range(n)]
    check = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0])
    dist[0][0] = 2
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 1 or dist[nx][ny] != 0:
                continue
            dist[nx][ny] = dist[x][y]
            q.append([nx,ny])
    
    t = False
    
    one_count = 0    
    for b in board:
        for index in b:
            if index == 1:
                one_count += 1

    for i in range(n):
        for j in range(m):

            if dist[i][j] != 2:
                continue
            # 상
            if i-1 >= 0:
                if board[i-1][j] == 1 and check[i-1][j] == 0:
                    check[i-1][j] = 1
                    board[i-1][j] = 0
                    t = True
            # 하
            if i+1 < n:
                if board[i+1][j] == 1 and check[i+1][j] == 0:
                    check[i+1][j] = 1
                    board[i+1][j] = 0
                    t = True
            # 좌
            if j-1 >= 0:
                if board[i][j-1] == 1 and check[i][j-1] == 0:
                    check[i][j-1] = 1
                    board[i][j-1] = 0
                    t = True
            # 우
            if j+1 < m:
                if board[i][j+1] == 1 and check[i][j+1] == 0:
                    check[i][j+1] = 1
                    board[i][j+1] = 0
                    t = True
    
    
    if one_count != 0:
        one = one_count


    if t:
        cnt += 1
    else:
        break                 

print(cnt)
print(one)