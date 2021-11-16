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

for i in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for index, num in enumerate(tmp):
        if num == 1:
            cheese.append([i,index])
answer = 0
while True:
    new_board = deepcopy(board)
    while cheese:
        x,y = cheese.popleft()
        cnt = 0
        for cur in range(4):
            nx = x + dx[cur]
            ny = y + dy[cur]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    cnt += 1
        if cnt >= 2:
            new_board[x][y] = 0
    flag = True
    for check in new_board:
        print(check)
        if check.count(1) > 0:
            flag = False
    board = deepcopy(new_board)
    print()
    if flag:
        answer += 1
        break
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    cheese.append([i,j])
    print(cheese)
    answer += 1

print(answer)