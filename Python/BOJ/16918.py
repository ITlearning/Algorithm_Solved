# 봄버맨
from collections import deque
from copy import deepcopy
R,C,N = map(int,input().split())
q = deque()
board = []

dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(R):
    tmp = list(input().rstrip())
    board.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == "O":
            q.append([i,j])

all_circle = [["O" for _ in range(C)] for _ in range(R)]
cnt = 0
while cnt < N:
    if cnt == 0:
        cnt += 1
        continue

    if cnt % 2 == 1:
        board = deepcopy(all_circle)
        cnt += 1
        continue

    while q:
        x,y = q.popleft()
        board[x][y] = "."
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == 'O':
                    board[nx][ny] = '.'
    
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                q.append([i,j])

    cnt += 1
    

for bo in board:
    print("".join(bo))
    


        
      