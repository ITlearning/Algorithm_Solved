# 입국심사
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

board = []

for i in range(n):
    tmp = int(input())
    board.append(tmp)

start = 1
end = m*max(board)
result = 0

while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in board:
        total += mid//i
    if total < m:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)
