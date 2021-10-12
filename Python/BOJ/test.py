from collections import Counter

board = [[0,0,0], [1,1,1], [2,2,2]]

for i in range(len(board[0])):
    tmp = []
    for j in range(len(board)):
        tmp.append(board[j][i])
    print(tmp)