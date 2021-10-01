# 예산
import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int,input().split()))
m = int(input())

start = 0
end = max(board)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in board:
        if mid <= i:
            total += mid
        else:
            total += i
    #print(start, end, mid ,total)

    if total > m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
print(answer)