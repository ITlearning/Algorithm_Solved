# 과자 나눠주기
import sys
input = sys.stdin.readline
M,N = map(int,input().split())

board = list(map(int,input().split()))

result = 0
start = 1
end = max(board)

while start <= end:
    cnt = 0
    mid = (start+end) // 2
    for i in board:
        cnt += i//mid
    if cnt >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)