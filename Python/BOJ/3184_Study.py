# 양 
from collections import deque
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
board = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]
sheep = 0
wolf = 0

for i in range(R):
    tmp = list(input().rstrip())
    board.append(tmp)

dist = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        # 벽 이거나 이미 방문했으면 continue
        if board[i][j] == '#' or dist[i][j] == 1:
            continue

        q = deque()
        q.append([i,j])
        dist[i][j] = 1
        sh_cnt = 0
        wl_cnt = 0
        
        while q:
            x,y = q.popleft()
            if board[x][y] == 'o':
                sh_cnt += 1
            elif board[x][y] == 'v':
                wl_cnt += 1
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if dist[nx][ny] == 1 or board[nx][ny] == '#':
                    continue
                dist[nx][ny] = 1
                q.append([nx,ny])

        if sh_cnt > wl_cnt:
            sheep += sh_cnt
        else:
            wolf += wl_cnt

print(sheep,wolf)
