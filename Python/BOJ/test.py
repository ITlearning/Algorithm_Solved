# 청소기
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
r,c, rotate = map(int,input().split())
board = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
    board.append(list(map(int,input().split())))

def turn():
    global rotate
    rotate = (rotate-1) % 4


cnt = 1
x,y = r,c
board[x][y] = 2
while True:
    t = True
    for i in range(4):
        turn()
        nx = x + dx[rotate]
        ny = y + dy[rotate]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0:
                cnt += 1
                board[nx][ny] = 2
                x,y = nx,ny
                t = False
                break
    if t:
        nx = x - dx[rotate]
        ny = y - dy[rotate]
        if 0 <= nx < n or 0 <= ny < m:
            if board[nx][ny] == 2:
                x,y = nx,ny
            elif board[nx][ny] == 1:
                print(cnt)
                break
        else:
            print(cnt)
            break

                