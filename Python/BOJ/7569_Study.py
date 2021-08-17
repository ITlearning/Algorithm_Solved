# 토마토
import sys
from collections import deque
input = sys.stdin.readline
m,n,h = map(int,input().split()) 
board = []

# 모두 6개의 위치를 따져야 하니 6개의 리스트들로 구성
dx = [0,-1,0,1,0,0]
dy = [-1,0,1,0,0,0]
dz = [0,0,0,0,-1,1]

# board 정보 리스트 저장
for i in range(h) :
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
    board.append(tmp)

# 1이 있는 위치 덱에 따로 저장
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                q.append((i,j,k))

# 덱에 저장된 위치를 하나씩 돌아본다.
while q:
    z,x,y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
            continue
        if board[nz][nx][ny] == 0:
            # 돌 때 board의 수를 하나씩 증가시켜 횟수 정보를 업데이트 한다.
            board[nz][nx][ny] = board[z][x][y] + 1
            q.append((nz,nx,ny))


total = 0 # 답이 될 변수
t = True  # 0 체크용

# 돌면서 0이 있을 경우엔 False를 반환해주고,
# 그게 아니면 제일 큰 숫자를 리턴해준다.
# 큰 숫자가 횟수의 마지막일테니
for z in board:
    for x in z:
        for y in x:
            if y == 0:
                t = False
            total = max(total, y)


# 0이면 -1, 아니면 total-1 출력
if t:
    print(total-1)
else:
    print(-1)

# 파이썬 3 : 시간초과
# 파이파이 3 : 848ms 통과