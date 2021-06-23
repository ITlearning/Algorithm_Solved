# 좌표 정렬하기
import sys
input = sys.stdin.readline
n = int(input())

board = []
for i in range(n):
    a,b = map(int, input().split())
    board.append([a,b])

board.sort(key=lambda x: (x[0],x[1]))

for i in board:
    print(i[0], i[1])