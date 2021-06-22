
N,M = map(int,input().split())
x,y,cur = map(int,input().split())
dist = [[0]*(M) for _ in range(N)]
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

# 북 동 남 서 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 출발하는 위치 방문 처리
dist[x][y] = 1

# 바라보는 방향 돌려주기
# 방향 돌리는거 기억합시다.
def turn():
    global cur
    cur -= 1
    if cur == -1:
        cur = 3

cnt = 1
time = 0
while True:
    turn()
    nx = x + dx[cur]
    ny = y + dy[cur]
    if dist[nx][ny] == 0 and board[nx][ny] == 0:
        x = nx
        y = ny
        dist[nx][ny] = 1
        cnt += 1
        time = 0
        continue
    else:
        time += 1
        if time == 4:
            nx = x - dx[cur]
            ny = y - dx[cur]
            if board[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            time = 0

print(cnt)