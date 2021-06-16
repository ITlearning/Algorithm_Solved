# 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[] for i in range(n+1)]
saving = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    board[a].append(b)
    board[b].append(a)
path = [1]
while path:
    node = path.pop()
    for i in board[node]:
        saving[i].append(node)
        path.append(i)
        board[i].remove(node)

for i in range(2,len(saving)):
    print(saving[i][0])