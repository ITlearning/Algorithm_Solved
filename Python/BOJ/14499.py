# 주사위 굴리기
import sys
from collections import deque
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())

board = [] # 지도

    # 동 서 북 남
dx = [0,0,-1,1]
dy = [1,-1,0,0]

dir_x = deque([0,0,0,0]) # 주사위 전개도 가로 부분
dir_y = deque([0,0,0,0]) # 주사위 전개도 세로 부분


# 그냥 인덱스를 키워드로 저장하여 사용할 때 직관적으로 보이게 설정
bottom = 1 # 주사위 밑 부분 인덱스
top = 3    # 주사위 윗 부분 인덱스

# 지도 생성
for i in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)

# 상하좌우 입력 커맨드들
cur = list(map(int,input().split()))

# 인덱스 이동을 위해 받은 숫자에서 하나씩 빼줌
for i in range(len(cur)):
    cur[i] -= 1

answer = [] # 답 리스트

# 입력받은 커맨드들을 하나씩 돌리며 시작
for dir in cur:
    
    # 이동한 위치가 지도 밖이라면 아무것도 하지 않음
    if x + dx[dir] < 0 or y + dy[dir] < 0 or x + dx[dir] >= n or y + dy[dir] >= m:
        continue
    
    # 아니면 일단 이동시키기
    x += dx[dir]
    y += dy[dir]

    # 좌 우 입력시 구현 기능
    if dir == 0 or dir == 1:
        # 동쪽은 인덱스를 하나씩 시계방향으로 밀어준다.
        if dir == 0:
            dir_x.appendleft(dir_x.pop())
        # 서쪽은 반시계방향으로
        elif dir == 1:
            dir_x.append(dir_x.popleft())
        
        # 주사위 바닥이 0이고 보드가 0이 아닐 경우와, 주사위 바닥이 0이 아니고 보드도 0이 아닐 경우도 같이 취급한다.
        if (dir_x[bottom] == 0 and board[x][y] != 0) or (dir_x[bottom] != 0 and board[x][y] != 0):
            dir_x[bottom] = board[x][y]
            board[x][y] = 0
        # 주사위 바닥이 0이 아니고 보드가 0 일경우
        elif dir_x[bottom] != 0 and board[x][y] == 0:
            board[x][y] = dir_x[bottom]

        # y 리스트와 주사위 아래 위 동기화
        dir_y[bottom] = dir_x[bottom]
        dir_y[top] = dir_x[top]

        # 그리고 답은 이동시킨 인덱스의 윗 부분 값
        answer.append(dir_x[top])
    

    # 상 하 입력시 구현 기능
    if dir == 2 or dir == 3:
        # 위쪽은 반시계방향으로
        if dir == 2:
            dir_y.append(dir_y.popleft())
        # 아래쪽은 시계방향으로
        elif dir == 3:
            dir_y.appendleft(dir_y.pop())
        
        # 주사위 바닥이 0이고 보드가 0이 아닐 경우와, 주사위 바닥이 0이 아니고 보드도 0이 아닐 경우도 같이 취급한다.
        if (dir_y[bottom] == 0 and board[x][y] != 0) or (dir_y[bottom] != 0 and board[x][y] != 0):
            dir_y[bottom] = board[x][y]
            board[x][y] = 0
        # 주사위 바닥이 0이 아니고 보드가 0 일경우
        elif dir_y[bottom] != 0 and board[x][y] == 0:
            board[x][y] = dir_y[bottom]

        # x 리스트와 주사위 아래 위 동기화
        dir_x[bottom] = dir_y[bottom]
        dir_x[top] = dir_y[top]

        # 답은 이동시킨 인덱스 윗 부분 값
        answer.append(dir_y[top])

# 답 출력
for i in answer:
    print(i)