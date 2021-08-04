# 스네이크 버드
N,L = map(int,input().split())

board = list(map(int,input().split()))
board.sort()
for i in range(N):
    if board[i] <= L:
        L += 1
print(L)