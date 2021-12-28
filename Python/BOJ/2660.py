# 회장 뽑기
n = int(input())
board = [[999999999 for _ in range(n+1)] for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0 으로 초기화
for i in range(1,n+1):
    board[i][i] = 0

# 입력받기
while True:
    x,y = map(int,input().split())
    # x 가 -1 나오면 종료
    if x == -1:
        break
    # 그게 아니면 시작 숫자가 1이었으니 1로 초기화
    board[x][y] = 1
    board[y][x] = 1

# 플루이드 워셜 알고리즘에 의해서 2차원 리스트를 방문하는 것을 따져가며 계산.
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            # 방문한 곳의 a,b 값을 더한 것이 현재 위치의 값보다 작다면 갱신
            board[a][b] = min(board[a][b], board[a][k] + board[b][k])

for i in board:
    print(i)

# 작은 수를 도출할 곳 
min_num = 999999999

for i in range(1,n+1):
    # 각 리스트에서 가장 큰 수와 min_num과 비교해서 작은 수 (1은 자기 자신의 숫자니 제외되는 느낌)
    min_num = min(min_num, max(board[i][1:]))
answer = []

# 작은 수와 같은 배열이라면
for i in range(1,n+1):
    if min_num == max(board[i][1:]):
        # 추가
        answer.append(i)

answer.sort() # 정렬

# 답 도출
print(min_num, len(answer))
print(*answer)