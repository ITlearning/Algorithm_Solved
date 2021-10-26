# 한 줄로 서기
n = int(input())

board = [0] * n

tmp = list(map(int,input().split()))

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == tmp[i] and board[j] == 0:
            board[j] = i + 1
            break
        elif board[j] == 0:
            cnt += 1

print(*board)