# 덩치
import sys
input = sys.stdin.readline
N = int(input())
board = []
for i in range(N):
    weight, height = map(int,input().split())
    board.append([weight,height])

for i in board:
    rank = 1
    for j in board:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
