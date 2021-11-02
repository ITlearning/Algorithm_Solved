# 불
import sys
from collections import deque
input = sys.stdin.readline

test = int(input())

dx = [0,-1,0,1]
dy = [-1,0,1,0]


def fdfs():
    global fire, fire_dist, board
    while fire:
        fx,fy = fire.popleft()
        for fi in range(4):
            nx = fx + dx[fi]
            ny = fy + dy[fi]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if fire_dist[nx][ny] >= 0 or board[nx][ny] == '#':
                continue
            fire_dist[nx][ny] = fire_dist[fx][fy] + 1
            fire.append([nx,ny])

def person_dfs():
    global person_dist, sang_geun, board
    while sang_geun:
        sx,sy = sang_geun.popleft()
        for si in range(4):
            nx = sx + dx[si]
            ny = sy + dy[si]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                return person_dist[sx][sy] + 1
            if person_dist[nx][ny] >= 0 or board[nx][ny] == '#':
                continue
            if fire_dist[nx][ny] != -1 and fire_dist[nx][ny] <= person_dist[sx][sy] + 1:
                continue
            person_dist[nx][ny] = person_dist[sx][sy] + 1
            sang_geun.append([nx,ny])
    return -1

# 불
for _ in range(test):
    w,h = map(int,input().split())
    board = []
    sang_geun = deque()
    fire = deque()
    fire_dist = [[-1 for _ in range(w)] for _ in range(h)]
    person_dist = [[-1 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        tmp = list(input().rstrip())
        board.append(tmp)
        for j in range(len(tmp)):
            if board[i][j] == '*':
                fire.append([i,j])
                fire_dist[i][j] = 0
            if board[i][j] == '@':
                sang_geun.append([i,j])
                person_dist[i][j] = 0
    fdfs()
    total = person_dfs()
    if total == -1:
        print("IMPOSSIBLE")
    else:
        print(total)
