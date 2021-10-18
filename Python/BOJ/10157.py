# 자리배정

# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

c,r = map(int,input().split())

target = int(input())

board = [[0 for _ in range(c)] for _ in range(r)]

x,y = r-1, 0
board[x][y] = 1
if r*c >= target:
    dir = 0
    while True:
        if board[x][y] == target:
            print(y+1,r-x)
            break
        tmp_x = x + dx[dir]
        tmp_y = y + dy[dir]
        if tmp_x >= 0 and tmp_y >= 0 and tmp_x < r and tmp_y < c:
            if board[tmp_x][tmp_y] == 0:
                board[tmp_x][tmp_y] = board[x][y] + 1
                x += dx[dir]
                y += dy[dir]
            else:
                dir = (dir+1) % 4
        else:
            dir = (dir+1) % 4
else:
    print(0)