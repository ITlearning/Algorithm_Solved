# 텀 프로젝트
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
    global ans
    dist[n] = True
    loop.append(n)
    num = board[n]
    if dist[num]:
        if num in loop:
            ans += loop[loop.index(num):]
        return
    else:
        dfs(num)

for _ in range(int(input())):
    n = int(input())
    board = [0] + list(map(int,input().split()))
    print(board)
    dist = [True] + [False] * (n)
    ans = list()

    for i in range(1,n+1):
        if not dist[i]:
            loop = list()
            dfs(i)
    print(n - len(ans))