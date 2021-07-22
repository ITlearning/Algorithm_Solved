# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(input())
board = []

for i in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)
q = deque()
an = []
start_x = 0
start_y = 0
for x in range(n):
    for y in range(n):
        if board[x][y] == 9:
            start_x = x
            start_y = y
            # 9가 나중에 물고기로 인식될수도 있으니 0으로 변경 해줘야 한다.
            board[x][y] = 0
            break

shark_size = 2
eat = 0
move = 0

while True:
    q = deque()
    q.append([start_x,start_y, 0])
    dist = [[False]*n for _ in range(n)]
    flag = 1e9
    an = []
    while q:
        x,y, cnt = q.popleft()

        # 만일 아기상어보다 작은 물고기를 먹었을 경우, flag가 제일 큰 값에서 cnt-1로 초기화 됐을 것
        # 따라서 먹고 난 뒤에는 종료
        if cnt > flag:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] > shark_size or dist[nx][ny]:
                continue
            # 0보다 크고 상어 크기보다 작을 경우
            if board[nx][ny] != 0 and board[nx][ny] < shark_size:
                # 먹기 리스트 저장
                an.append([nx,ny, cnt+1])
                # 저장했으면 flag 초기화
                flag = cnt
            # 방문 표시
            dist[nx][ny] = True
            # 일단 모든 bfs 돈 값 덱에 저장
            q.append([nx,ny,cnt+1])

    # 그리고 난 뒤에 일단 상어보다 작은 건 다 an에 저장되어있을 테니, 그 중 오름차순으로 정렬해 작은 걸 + 해줌.
    if len(an) > 0:
        an.sort()
        x,y, m = an[0][0], an[0][1], an[0][2]
        move += m
        eat += 1
        # 먹은것은 0으로 변경해준다.
        board[x][y] = 0
        # 하나하나 먹는데, 먹은 횟수가 크기와 같아졌을 경우
        if eat == shark_size:
            # 상어 크기를 +1 해주고 먹은 것을 초기화 해준다.
            shark_size += 1
            eat = 0
        # 그리고 먹은 곳으로 다시 위치를 변경 해준다.
        start_x, start_y = x,y
    else:
        # 만약 더이상 먹을게 없으면 break
        break


print(move)