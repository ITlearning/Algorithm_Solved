# 지구 온난화
r,c = map(int,input().split())

board = []

dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(r):
    board.append(list(str(input())))

print(board)