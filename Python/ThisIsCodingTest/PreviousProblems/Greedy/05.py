n,m = map(int, input().split())
count = 0
board = list(map(int, input().split()))

for i in range(len(board)):
    for j in range(i,len(board)):
        if i <= m and j <= m:
            if board[i] != board[j] :
                count += 1

print(count)