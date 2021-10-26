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
    for i in board: # for문 돌면서 전체 값과 mid값을 나눠주고 반올림 한다.
        total += ceil(i/mid)
    # 그렇게 나온 값이 n개보다 클 경우에는 start 개수 늘려주고
    if total > n:
        start = mid + 1
    else: # 아니면 답에 원래 입력했던 것보다 작을 시 변경
        answer = min(answer, mid)
        end = mid - 1

print(answer)