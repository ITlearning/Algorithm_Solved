# 입국심사

n,m = map(int,input().split())

board = []
for _ in range(n):
    tmp = int(input())
    board.append(tmp)

total = 0
start = 0
# 입력받은 m과 입력받은 리스트 중 가장 큰 수
end = m*max(board)

while start <= end:
    mid = (start + end) // 2
    passing = 0
    for i in board:
        passing += mid // i
    # 통과한 사람의 수가 입력받은 수보다 작을 경우
    if passing < m:
        start = mid + 1
    else:
        # 클 경우
        total = mid
        end = mid - 1

print(total)