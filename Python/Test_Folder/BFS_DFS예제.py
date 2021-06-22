import sys
from collections import deque
input = sys.stdin.readline
N,M,V = map(int,input().split())

board = [[0]*(N+1) for _ in range(N+1)]
dist = [False] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    board[a][b] = board[b][a] = 1



def DFS(V):
    dist[V] = True
    print(V, end=' ')
    for i in range(1,N+1):
        if dist[i] == False and board[V][i] == 1:
            DFS(i)


def BFS(V):
    q = [V]
    dist[V] = False
    while q:
        V = q.pop(0)
        print(V, end=' ')
        for i in range(1,N+1):
            if board[V][i] == 1 and dist[i] == True:
                dist[i] = False
                q.append(i)


DFS(V)
print()
BFS(V)