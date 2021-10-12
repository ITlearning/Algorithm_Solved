# 에라토스테네스의 체
n,k = map(int,input().split())

board = [True] * (n+1)
cnt = 0
for i in range(2, len(board)+1):
    for j in range(i, n+1, i):
        if board[j] == True:
            board[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                break