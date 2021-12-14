# 캐슬 디펜스
from itertools import combinations
from heapq import heappop, heappush
import copy
n,m,d = map(int,input().split())
arrows_list = [i for i in range(m)]
arrows = tuple(combinations(arrows_list, 3))
insert = [list(map(int, input().rstrip().split())) for _ in range(n)]
board = []

def count_enemy():
    global board 
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 :
                cnt += 1
    
    return cnt

def attack(arrow_index):
    global board
    attack_list = []
    visited = [[False for _ in range(m)] for _ in range(n)]

    cnt = 0

    for arrow in arrows[arrow_index]:
        q = [] # [거리, x,y] 우선순위 큐에 삽입

        for i in range(n-1, -1, -1):
            for j in range(m):
                if board[i][j] == 1:
                    tmp = abs(n-i) + abs(arrow - j)
                    if tmp <= d:
                        heappush(q, [tmp,j,i])
        
        if q:
            distance,x,y = heappop(q)
            attack_list.append([y,x])

    for y,x in attack_list:
        if not visited[y][x]:
            visited[y][x] = True
            cnt += 1
            board[y][x] = 0

    return cnt

def move():
    global board
    board[-1] = [0 for _ in range(m)]

    for i in range(-1, -n, -1):
        board[i] = board[i-1]
    
    board[0] = [0 for _ in range(m)]


def start(arrow_index):
    cnt = 0

    while count_enemy() != 0:
        cnt += attack(arrow_index)
        move()
    
    return cnt

answer = 0
for i in range(len(arrows)):
    board = [[insert[i][j] for j in range(m)] for i in range(n)]
    cnt = start(i)
    if answer < cnt:
        answer = cnt

print(answer)