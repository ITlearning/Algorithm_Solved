# 탈출
from collections import deque
r,c = map(int,input().split())

q = deque()
board = []

dist = [[0 for _ in range(c)] for _ in range(r)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

# 비버집 위치 저장 클래스
class beaver_home:
    x = 0
    y = 0

# 1. 입력받기
for i in range(r):
    tmp = list(input())
    board.append(tmp)

# 2. 입력받은 각 위치 저장하기
for i in range(r):
    for j in range(c):
        if board[i][j] == 'D':
            beaver_home.x = i
            beaver_home.y = j
        if board[i][j] == 'S':
            q.append([i,j])

# 2-1. 물의 위치는 여러개 있을 수 있으니, 따로 저장해주기      
for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            q.append([i,j])

# 비버집 정상적으로 도착했는지 여부 확인 Bool
flag = False

# 덱 돌리기 시작
while q:
    x,y = q.popleft()

    # 만일 비버집 위치가 S(고슴도치)로 바뀌었을 경우
    if board[beaver_home.x][beaver_home.y] == 'S':
        # 플래그 바꾸고 종료
        flag = True
        break

    # 상,하,좌,우 돌면서 체크
    for cur in range(4):
        nx = x + dx[cur]
        ny = y + dy[cur]
        
        if 0 <= nx < r and 0 <= ny < c:
            # 만일 공백위치 이거나 비버의 집이고 지금 뽑은 위치에 고슴도치가 있다면
            if (board[nx][ny] == '.' or board[nx][ny] == 'D') and board[x][y] == 'S':
                # 인접한 곳은 갈 수 있는 곳이니 거기 글자를 고슴도치 표시로 바꿈
                board[nx][ny] = 'S'
                # 움직인 거리 증가
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])
            # 만일 공백위치 이거나 고슴도치가 방문한 위치 둘 중 하나이고 동시에 지금 뽑았던 위치가 물이 지나갔던 위치라면
            elif (board[nx][ny] == '.' or board[nx][ny] == 'S') and board[x][y] == '*':
                # 인접한 곳은 갈 수 있는 곳이니 인접한 곳에 글자를 물로 바꿈
                board[nx][ny] = '*'
                q.append([nx,ny])

# 플래그가 True일 경우에
if flag:
    # 거리 출력
    print(dist[beaver_home.x][beaver_home.y])
else:
    # 그게 아니면 아래 문구 출력
    print("KAKTUS")