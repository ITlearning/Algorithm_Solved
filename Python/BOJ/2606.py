# 바이러스
import sys
input = sys.stdin.readline
n = int(input())
v = int(input())
board = []
graph = {}

for _ in range(v) :
    a,b = map(int, input().split())
    board.append([a,b])

for i,j in board:
    # get 함수를 사용하여 i,j의 value값을 가져와서 합쳐주기
    graph[i] = graph.get(i, []) + [j]
    graph[j] = graph.get(j, []) + [i]

# 재귀적으로 인덱스를 지난다.
def dfs(start, graph):
    # for문을 돌며 지나간 인덱스가 아닐 경우 추가 해주고, 재귀적으로 해당 인덱스를 돈다.
    for i in graph[start]:
        if i not in dist:
            dist.append(i)
            dfs(i, graph)

dist = []
dfs(1, graph)

print(len(dist)-1)