# 맥주 마시면서 걸어가기
from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

def bfs(x,y):
    q,c = deque(), []
    q.append([x,y, 20])
    c.append([x,y, 20])
    while q:
        x, y, beer = q.popleft()
        if x == x1 and y == y1:
            print("happy")
            return
        for nx,ny in board:
            if [nx,ny,20] not in c:
                l1 = abs(nx - x) + abs(ny - y)
                if beer * 50 >= l1:
                    q.append([nx,ny,20])
                    c.append([nx,ny,20])
    print("sad")
    return

while t:
    n = int(input())
    input_x, input_y = map(int,input().split())
    board = []
    for _ in range(n):
        x,y = map(int,input().split())
        board.append([x,y])
    x1,y1 = map(int,input().split())
    board.append([x1,y1])
    bfs(0,0)
    t -= 1
