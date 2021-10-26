# 지구 온난화
r,c = map(int,input().split())

board = []

dx = [0,-1,0,1]
dy = [-1,0,1,0]
# 1. 입력
for i in range(r):
    board.append(list(str(input())))

delete = []

# 2. 돌리면서 X가 있을 경우 상하좌우 돌면서 3개 이상 바다가 존재하는 경우 추가
for i in range(r):
    for j in range(c):
        if board[i][j] == "X":
            cnt = 0
            for dir in range(4):
                nx = i + dx[dir]
                ny = j + dy[dir]
                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    cnt += 1
                    continue
                if board[nx][ny] != ".":
                    continue
                cnt += 1
            if cnt >= 3:
                delete.append([i,j])

# 3. 해수면 상승으로 지워질 섬을 .으로 변경
for x,y in delete:
    board[x][y] = "."

# 시작 x,y 끝 x,y 저장 변수
start_x = 99999999999
end_x = 0
start_y = 99999999999
end_y = 0

# 4. 돌면서 X가 처음 시작하는 곳, 끝나는 곳을 저장
for i in range(r):
    for j in range(c):
        if board[i][j] == "X":
            start_x = min(start_x, i)
            start_y = min(start_y, j)
            end_x = max(end_x,i)
            end_y = max(end_y,j)

# 5. X의 시작과 끝으로 for문 돌려서 새로운 직사각형 만들기
for i in range(start_x, end_x+1):
    for j in range(start_y, end_y+1):
        print(board[i][j], end="")
    print()