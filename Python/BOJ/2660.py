# 회장 뽑기

n = int(input())
board = [[999999999 for _ in range(n+1)] for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0 으로 초기화
for i in range(1,n+1):
    board[i][i] = 0

while True:
    x,y = map(int,input().split())
    if x == -1:
        break
    board[x][y] = 1
    board[y][x] = 1


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            board[a][b] = min(board[a][b], board[a][k] + board[b][k])

min_num = 999999999

for i in range(1,n+1):
    # 각 리스트에서 가장 큰 수와 min_num과 비교해서 작은 수 (1은 자기 자신의 숫자니 제외되는 느낌)
    min_num = min(min_num, max(board[i][1:]))
answer = []
for i in range(1,n+1):
    if min_num == max(board[i][1:]):
        answer.append(i)

answer.sort()
print(min_num, len(answer))
print(*answer)