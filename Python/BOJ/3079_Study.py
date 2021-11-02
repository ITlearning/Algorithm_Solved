# 입국심사
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

board = []

for i in range(n):
    tmp = int(input())
    board.append(tmp)

start = 1
end = m*max(board) # 모든 인원 * 최대 심사대 시간
result = 0

while start <= end:
    mid = (start+end) // 2
    total = 0
    # board 돌리면서 각 심사대에서 뽑아낼 수 있는 사람의 수 계산
    for i in board:
        total += mid//i
    # 그게 m 보다 작으면 start 늘리기
    if total < m:
        start = mid + 1
    else: # 그게 아니면 답 입력하고 end 줄이기
        result = mid
        end = mid - 1

print(result)
