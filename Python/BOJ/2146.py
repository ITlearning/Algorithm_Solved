# 다리 만들기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
cnt_dist = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 섬이 몇개 있는지 BFS로 구하기
def bfs(x,y,cnt):
    cnt_dist[x][y] = cnt
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] == 0 or cnt_dist[nx][ny] == cnt:
                continue
            cnt_dist[nx][ny] = cnt
            q.append((nx,ny))


# 섬 중에서 하나를 선택해서 섬의 크기를 늘려간다.
# 이때 다른섬에 닿을 경우 그때 까지의 거리를 리턴
def bfs2(num):
    while q2:
        x,y = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if board[nx][ny] == 1 and cnt_dist[nx][ny] != num:
                return box_dist[x][y] - 1
            if board[nx][ny] == 0 and box_dist[nx][ny] == 0:
                box_dist[nx][ny] = box_dist[x][y] + 1
                q2.append((nx,ny))


cnt = 1
# 위에서 첫 번째로 생성한 bfs 를 돌리면서 해당 섬이 몇번째 섬인지 기록
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and cnt_dist[i][j] == 0:
            bfs(i,j,cnt)
            cnt += 1

# 그리고 기록한 섬들을 가지고, 하나씩 돌아보는거다.
# 돌리면서 섬을 점점 키우고, 키우다가 다른 섬을 만날 경우에 커지고 있던 길이를 리턴
answer = 9999999999
for k in range(1, cnt):
    q2 = deque()
    box_dist = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 and cnt_dist[i][j] == k:
                q2.append((i,j))
                box_dist[i][j] = 1
    # 돌면서 제일 작은 길이를 answer에 기록
    res = bfs2(k)
    answer = min(answer, res)
# 답
print(answer)