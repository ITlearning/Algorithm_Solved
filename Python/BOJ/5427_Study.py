# 불
import sys
from collections import deque
input = sys.stdin.readline

test = int(input())

dx = [0,-1,0,1]
dy = [-1,0,1,0]

# 불 확인하는 dfs
# 불의 방문 시간을 먼저 구한다.
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


# 사람 확인하는 dfs
# 불이 방문한 시간을 비교해서 불보다 클 경우에는 못나가는거니까
# 그거 아니면 계속 움직이기
def person_dfs():
    global person_dist, sang_geun, board
    while sang_geun:
        sx,sy = sang_geun.popleft()
        for si in range(4):
            nx = sx + dx[si]
            ny = sy + dy[si]
            # 탈출 성공하면 리턴
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                return person_dist[sx][sy] + 1
            if person_dist[nx][ny] >= 0 or board[nx][ny] == '#':
                continue
            # 방문을 했거나, 불의 방문 시간보다 사람의 방문 시간이 더 크면 그건 못지나가는 곳이니까 continue
            if fire_dist[nx][ny] != -1 and fire_dist[nx][ny] <= person_dist[sx][sy] + 1:
                continue
            # 그거 아니면 움직이기~
            person_dist[nx][ny] = person_dist[sx][sy] + 1
            sang_geun.append([nx,ny])
    # 답 없으면 -1 리턴
    return -1

# main
for _ in range(test):
    w,h = map(int,input().split())
    board = []
    sang_geun = deque()
    fire = deque()
    # 둘 -1로 초기화
    fire_dist = [[-1 for _ in range(w)] for _ in range(h)]
    person_dist = [[-1 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        tmp = list(input().rstrip())
        board.append(tmp)

        # 불, 상근 위치 기록
        for j in range(len(tmp)):
            if board[i][j] == '*':
                fire.append([i,j])
                fire_dist[i][j] = 0
            if board[i][j] == '@':
                sang_geun.append([i,j])
                person_dist[i][j] = 0
    # 각 로직 수행
    fdfs()
    total = person_dfs()

    # total 값이 -1 이면 IMPOSSIBLE, 아니면 total 값 도출
    if total == -1:
        print("IMPOSSIBLE")
    else:
        print(total)
