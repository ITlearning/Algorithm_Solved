# 치즈
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]
board = []
cheese = deque()
air_deque = deque()

for i in range(n):
    tmp_cheese = list(map(int,input().split()))
    board.append(tmp_cheese)
    for tmp in range(len(tmp_cheese)):
        if tmp_cheese[tmp] == 1:
            cheese.append([i, tmp])
    
melt_count = 0
while True:
    # 공기 체크 (안에 있는 건지 아닌지)
    air_cnt = 0
    air = [[0 for _ in range(m)] for _ in range(n)]
    for air_x in range(n):
        for air_y in range(m):
            if board[air_x][air_y] != 0 or air[air_x][air_y] > 0:
                continue
            air[air_x][air_y] = air_cnt + 1
            air_deque.append([air_x, air_y])
            while air_deque:
                x,y = air_deque.popleft()
                for air_cur in range(4):
                    nx = x + dx[air_cur]
                    ny = y + dy[air_cur]
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 1 or air[nx][ny] != 0:
                            continue
                        air[nx][ny] = air[x][y]
                        air_deque.append([nx,ny])
            air_cnt += 1
            
    new_board = deepcopy(board)

    while cheese:
        cheese_x, cheese_y = cheese.popleft()
        sea_cnt = 0
        for ch_cur in range(4):
            nx = cheese_x + dx[ch_cur]
            ny = cheese_y + dy[ch_cur]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 or air[nx][ny] != 1:
                    continue
                sea_cnt += 1

        if sea_cnt >= 2:
            new_board[cheese_x][cheese_y] = 0

    board = deepcopy(new_board)

    for copy_x in range(n):
        for copy_y in range(m):
            if board[copy_x][copy_y] == 1:
                cheese.append([copy_x, copy_y])

    if len(cheese) == 0:
        print(melt_count+1)
        break

    melt_count += 1


