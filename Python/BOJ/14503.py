# 청소기
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
r,c, rotate = map(int,input().split())
board = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
    board.append(list(map(int,input().split())))

# 보는 방향 돌려주기
def turn():
    global rotate
    rotate = (rotate-1) % 4
# 초기 카운트
cnt = 1
# r,c를 x,y로 바꿈
x,y = r,c
# 처음 시작하는 곳을 청소
board[x][y] = 2
# 벽 만나거나 작동 불가할때까지 돌림
while True:
    # 이동을 했는지 안했는지 확인
    t = False
    for i in range(4):
        # 4면 보기
        turn()
        nx = x + dx[rotate]
        ny = y + dy[rotate]
        if 0 <= nx < n and 0 <= ny < m:
            # 만약에 청소 안했으면
            if board[nx][ny] == 0:
                cnt += 1
                board[nx][ny] = 2
                x,y = nx,ny
                t = True
                break
    # 4면 다돌았는데도 청소할데가 없었다면
    if t == False:
        #일단 보는 방향대로 빼주기
        nx = x - dx[rotate]
        ny = y - dy[rotate]
        # 공간안에 위치하면
        if 0 <= nx < n and 0 <= ny < m:
            # 만일 움직인 곳이 청소한 곳이라면
            if board[nx][ny] == 2:
                # 빼준대로 일단 x,y 재설정
                x,y = nx,ny
            # 만일 그게 벽이라면
            elif board[nx][ny] == 1:
                # 카운트 출력하고 끝내기
                print(cnt)
                break
        else: # 공간안에 위치하지 않고 벗어나면
            # 출력하고 끝내기
            print(cnt)
            break