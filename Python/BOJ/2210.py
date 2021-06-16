# 숫자판 점프

board = []
for i in range(5):
    text = list(map(int,input().split()))
    board.append(list(text))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
value = []
def dfs(x,y, cnt, tmp):
    tmp += str(board[x][y])
    cnt += 1
    if cnt == 6:
        value.append(tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5: continue
        dfs(nx,ny,cnt,tmp)

for i in range(5):
    for j in range(5):
        dfs(i,j, 0, "")

print(len(set(value)))