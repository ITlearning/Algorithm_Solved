# <문제 - 미래도시>
# 개수의 제한이 100개라 플로이드 워셜 알고리즘을 사용해보겠다.
INF = int(1e9) # 무한 숫자 설정

n,m = map(int, input().split())
board = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 사신으로 가는 비용은 0
for a in range(n+1):
    for b in range(n+1):
        if a == b :
            board[a][b] = 0


for _ in range(m) :
    a,b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1
    # 문제에서 서로에게 가는 비용은 1이라고 적었으니 1로 갱신

x,k = map(int, input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

# 알고리즘을 수행한 후에 (1번 노드에서 X까지의 최단거리 + X에서 K까지의 최단 거리)
# 를 계산하여 출력하여야 한다.
result = board[1][k] + board[k][x]

if result >= INF:
    print("-1")
else:
    print(result)