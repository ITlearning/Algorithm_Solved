# 저울
import sys
input = sys.stdin.readline

N = int(input())

board = list(map(int,input().split()))
board.sort()
total = 1
for i in board:
    if total < i:
        break
    total += i

print(total)
'''
for i in range(0,N): # index
    for cur in range(1,N): #cursor
        for j in range(0,len(board), cur):
            if board[i] != board[j]:
                tmp = board[i] + sum(board[j:j+cur])
                if tmp not in total:
                    total.append(tmp)
total.sort()
print(total)
for i in total:
    if i+1 not in total:
        print(i+1)
        break
'''

