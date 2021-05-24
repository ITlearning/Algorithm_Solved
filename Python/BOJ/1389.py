#플로이드 - 워셜 알고리즘

from math import inf
n,m = map(int, input().split())

board = [[inf] * n for _ in range(n)]

for i in range(n) :
    board[i][i] = 0

for _ in range(m) :
    start, end = map(int, input().split())
    board[start-1][end-1] = 1
    board[end-1][start-1] = 1

# 모든 경우를 체크하면서 최솟값을 업데이트 해주는 알고리즘
for k in range(n):
    for a in range(n):
        for b in range(n):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

answer = inf
index = inf

for i in range(len(board)):
    if sum(board[i]) < answer:
        answer = sum(board[i])
        index = i

print(index+1)
# https://pacific-ocean.tistory.com/278

# https://donghak-dev.tistory.com/10