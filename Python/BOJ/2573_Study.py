# 빙산
import collections
import sys
from collections import deque
import copy
input = sys.stdin.readline
n,m = map(int,input().split())

board = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()

for i in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for index, num in enumerate(tmp):
        if num > 0:
            q.append([i, index])


a = 0
while True:
    q_cnt = len(q)
    another_q = deque()
    new_board = copy.deepcopy(board)
    while q:
        x,y = q.popleft()
        cnt = 0
        for cur in range(4):
            nx = x + dx[cur]
            ny = y + dy[cur]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    cnt += 1

        if board[x][y] - cnt >= 0:
            new_board[x][y] -= cnt
        else:
            new_board[x][y] = 0
    
    visited = [[0 for _ in range(m)] for _ in range(n)]

    board = copy.deepcopy(new_board)

    box_num = 0
    for ki in range(n):
        for kj in range(m):
            if board[ki][kj] > 0 and visited[ki][kj] == 0:
                another_q.append([ki,kj])
                visited[ki][kj] = 1
                box_num += 1
                while another_q:
                    ax, ay = another_q.popleft()
                    for an_dir in range(4):
                        zx = ax + dx[an_dir]
                        zy = ay + dy[an_dir]
                        if 0 <= zx < n and 0 <= zy < m:
                            if board[zx][zy] != 0 and visited[zx][zy] != 1:
                                another_q.append([zx,zy])
                                visited[zx][zy] = 1

    t = True
    for x_index in range(n):
        for y_index in range(m):
            if board[x_index][y_index] > 0:
                q.append([x_index,y_index])
                t = False
    
    if t:
        a = 0
        break

    if 1 != box_num:
        a += 1
        break

    a += 1

print(a)