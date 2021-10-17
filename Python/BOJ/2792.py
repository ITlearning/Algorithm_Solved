# 보석 상자
from math import ceil
n,m = map(int,input().split())
board = []

for _ in range(m):
    tmp = int(input())
    board.append(tmp)

start = 1
end = max(board)

answer = 999999999999

while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in board:
        total += ceil(i/mid)
    
    if total > n:
        start = mid + 1
    else:
        answer = min(answer, mid)
        end = mid - 1

print(answer)