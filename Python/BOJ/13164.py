# 행복 유치원

import sys
input = sys.stdin.readline
n,k = map(int,input().split())

board = list(map(int,input().split()))
dist = []
for i, j in zip(board, board[1:]):
    dist.append(j-i)

dist.sort()
for _ in range(k-1):
    dist.pop()


print(sum(dist))