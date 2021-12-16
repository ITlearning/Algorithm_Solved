# 나무조각

board = list(map(int,input().split()))
answer = [1,2,3,4,5]
while True:
    for i in range(len(board)-1):
        if board[i] > board[i+1]:
            board[i], board[i+1] = board[i+1], board[i]
            print(*board)
    
    if board == answer:
        break