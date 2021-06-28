# 스타트링크
import sys
from collections import deque
input = sys.stdin.readline
# F 빌딩의 총 층
# S 강호가 현재 위치하는 층
# G 스타트링크가 있는 층
# U 위로 U층 이동할 수 있는 수
# D 아래로 D층 이동할 수 있는 수
F,S,G,U,D = map(int,input().split())

q = deque()
q.append([S,0])

def dfs():
    dist = {S}
    while q:
        x, cnt = q.popleft()
        if x == G:
            return cnt
        if x + U <= F and x + U not in dist:
            q.append([x+U, cnt+1])
            dist.add(x+U)
        if x - D >= 1 and x - D not in dist:
            q.append([x-D, cnt + 1])
            dist.add(x-D)
    return "use the stairs"

print(dfs())