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
    if passing < m:
        start = mid + 1
    else:
        total = mid
        end = mid - 1

print(total)