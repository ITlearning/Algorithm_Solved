# 대표 자연수
import sys
import heapq
input = sys.stdin.readline

n = int(input())

board = list(map(int,input().split()))
total = []
for i in range(n):
    tmp = 0
    for j in board:
        tmp += abs(board[i] - j)
    heapq.heappush(total, [tmp,board[i]])

print(total[0][1])

# PyPy 통과