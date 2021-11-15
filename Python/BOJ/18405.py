# 경쟁적 전염
from collections import deque
n,m = map(int,input().split())

board = []
sort_list = []
sort = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for index, num in enumerate(tmp):
        if num > 0:
            sort_list.append([i,index,num])

sort_list.sort(key=lambda x : x[2])

q = deque(sort_list)
s,answer_x,answer_y = map(int,input().split())

time = 0
while time < s:
    time += 1
    cnt = len(q)
    while cnt > 0:
        x,y, pop_num = q.popleft()
        for cur in range(4):
            nx = x + dx[cur]
            ny = y + dy[cur]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = pop_num
                    q.append([nx,ny, pop_num])
        cnt -= 1
    cnt = len(q)

print(board[answer_x-1][answer_y-1])