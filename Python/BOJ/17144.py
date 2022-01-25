# 미세먼지 안녕!
from collections import deque
import sys
input = sys.stdin.readline

r,c,t = map(int,input().split())
dx = [0,-1,0,1]
dy = [-1,0,1,0]
air_cleaner = []
board = []
q = deque()

# 입력받기
for i in range(r):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        # -1 일경우엔 air_cleaner 리스트에 저장
        if tmp[j] == -1:
            air_cleaner.append(i)
        # 0 아니고 다른 숫자면 덱에 저장
        elif tmp[j] != 0:
            q.append([i,j])
    
    board.append(tmp)

# 덱에 먼지 위치 추가
def reset():
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                q.append([i,j])

# 먼지 분산
def dust():
    board_tmp = [[0 for _ in range(c)] for _ in range(r)]

    while q:
        x,y = q.popleft()
        num = board[x][y]
        divide_num = board[x][y] // 5
        for cur in range(4):
            nx = x + dx[cur]
            ny = y + dy[cur]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != -1:
                    board_tmp[nx][ny] += divide_num
                    num -= divide_num
        
        board_tmp[x][y] += num
    
    # 새로 생긴 리스트에 공기청정기 위치에 -1 해주기
    board_tmp[air_cleaner[0]][0] = -1
    board_tmp[air_cleaner[1]][0] = -1

    return board_tmp

# 공기청정기 작동
def work_air_cleaner(board):
    cleaner_up = air_cleaner[0]
    cleaner_down = air_cleaner[1]

    # 공기청정기 위쪽 공기 내리기
    for i in range(cleaner_up-1, 0, -1):
        board[i][0] = board[i-1][0]
    board[0][0] = 0

    # 공기청정기 아래쪽 공기 올리기
    for i in range(cleaner_down+2, r):
        board[i-1][0] = board[i][0]
    board[r-1][0] = 0

    # 왼쪽 이동
    for i in range(0, c-1):
        board[0][i] = board[0][i+1]
        board[r-1][i] = board[r-1][i+1]
    board[0][c-1] = 0
    board[r-1][c-1] = 0

    # 공기청정기 반대 위쪽 공기 올리기
    for i in range(0, cleaner_up):
        board[i][c-1] = board[i+1][c-1]
    board[cleaner_up][c-1] = 0

    # 공기청정기 반대 아래쪽 공기 내리기
    for i in range(r-1, cleaner_down, -1):
        board[i][c-1] = board[i-1][c-1]
    board[cleaner_down][c-1] = 0

    # 오른쪽 이동
    for i in range(c-1, 1, -1):
        board[cleaner_up][i] = board[cleaner_up][i-1]
        board[cleaner_down][i] = board[cleaner_down][i-1]

    
    board[cleaner_up][1] = 0
    board[cleaner_down][1] = 0

# 모든 먼지 값 구하기
def check():
    cnt = 0
    for i in range(r):
        cnt += sum(board[i])
    
    return cnt + 2

time = 0

# 입력받은 t까지 계속 돌리기
while time < t:
    board = dust()
    work_air_cleaner(board)
    reset()
    time += 1

answer = check()

print(answer)


