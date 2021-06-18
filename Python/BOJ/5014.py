# 스타트링크
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
F,S,G,U,D = map(int,input().split())

cnt = 0
def dfs(F,S,G,U,D):
    q = deque()
    q.append([S,0])
    dist = {S}
    while q:
        floor ,cnt = q.popleft()
        if floor == G:
            return cnt
        if floor + U <= F and floor + U not in dist:
            q.append([floor + U, cnt + 1])
            dist.add(floor + U)
        if floor - D >= 1 and floor - D not in dist:
            q.append([floor - D, cnt + 1])
            dist.add(floor - D)
    return "use the stairs"

print(dfs(F,S,G,U,D))