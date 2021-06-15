# 동전 0
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
board = []
for _ in range(n):
    board.append(int(input()))
board.sort()
cnt = 0
for i in board[::-1]:
    if i < k:
       cnt += k//i
       k -= i * (k//i)
print(cnt)