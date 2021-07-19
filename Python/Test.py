from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
q = []

def init():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 9:
                heappush(q, (0, i, j))
                a[i][j] = 0
                return

def bfs():
    body, eat, ans = 2, 0, 0
    check = [[False]*n for _ in range(n)]
    while q:
        d, x, y = heappop(q)
        if 0 < a[x][y] < body:
            eat += 1
            a[x][y] = 0
            if eat == body:
                body += 1
                eat = 0
            ans += d
            d = 0
            while q:
                q.pop()
            check = [[False]*n for _ in range(n)]
        for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
            nd, nx, ny = d+1, x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if 0 < a[nx][ny] > body or check[nx][ny]:
                continue
            check[nx][ny] = True
            heappush(q, (nd, nx, ny))
    print(ans)

init()
bfs()