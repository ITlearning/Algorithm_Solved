# 자리배정

# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

c,r = map(int,input().split())

target = int(input())

board = [[0 for _ in range(c)] for _ in range(r)]

# 1. 초기 위치 설정 (왼쪽 하단부터 시작하니까 왼쪽 하단 좌표)
x,y = r-1, 0
# 1-2. 초기위치부터 카운트
board[x][y] = 1

# 2. 만약에 target이 가로 세로 곱한 것 보다 작거나 같으면 while 문 돌림
if r*c >= target:
    dir = 0 # 방향 전환용 변수
    while True:
        if board[x][y] == target: # 만일 지금 좌표의 수가 target 수와 같으면
            print(y+1,r-x) # 좌표 출력하고 끝
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
else: # 2-2. 아니면 0 출력
    print(0)