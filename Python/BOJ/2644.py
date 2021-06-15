# 촌수계산
from collections import deque
import sys
input = sys.stdin.readline
# 입력 여러 조건들 입력 받기
p = int(input())
x,y = map(int,input().split())
people = int(input())

# 이어진 노드 저장 board리스트, 지나간 순서 저장할 dist
board = [[] for i in range(p+1)]
dist = [0] * (p+1)

# 이어진 노드들 끼리 저장
for _ in range(people):
    a,b = map(int,input().split())
    board[a].append(b)
    board[b].append(a)


# dfs global board, dist, x
def dfs(start):
    # 우리가 찾기 시작할 노드(x)부터 찾기 시작
    # 돌면서 i가 x 아니고 방문하지 않았으면 더해주고 다시 dfs돌림
    for i in board[start]:
        if i != x and dist[i] == 0:
            dist[i] = dist[start] + 1
            dfs(i)


# 아까 입력받은 x
dfs(x)

# 목표지점에서 방문카운트가 0이면 이어진게 아니니 -1 리턴
if dist[y] == 0:
    print(-1)
# 그게 아니면 값이 존재할꺼니까 dist[y] 값 출력
else:
    print(dist[y])

