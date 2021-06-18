# 쉽게 푸는 문제
import sys
input = sys.stdin.readline
A,B = map(int,input().split())
board = []
board.append(0)
for i in range(1000):
    for j in range(i):
        board.append(i)

num = 0
for i in range(A, B+1):
    num += board[i]
print(num)