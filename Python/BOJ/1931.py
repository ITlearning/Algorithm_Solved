# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp)

board.sort()
answer = 0
print(board)
for i in range(len(board)):
    an = 1
    check = board[i][1]
    for j in range(i,len(board)):
        print(check, board[j][0])
        if check <= board[j][0]:
            check = board[j][1]
            an += 1
    
    answer = max(answer, an)


print(answer)