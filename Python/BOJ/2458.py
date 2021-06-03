# 키 순서
# 플로이드 워셜 문제
# 키의 순서를 알 수 있다라는건 모든 노드들을 왔다갔다 할 수 있다라는 뜻
# 따라서 그거 아니면 카운트 하지 않으면 된다

import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int,input().split())
board = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b :
            board[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    board[a][b] = 1
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if board[a][b] == 1 or (board[a][k] == 1 and board[k][b] == 1):
                board[a][b] = 1

result = 0
for a in range(1,n+1):
    count = 0
    for b in range(1,n+1):
        if board[a][b] != INF or board[b][a] != INF:
            count += 1
    if count == n:
        result += 1

print(result)
