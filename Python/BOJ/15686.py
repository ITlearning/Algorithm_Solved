# 치킨 배달
from itertools import permutations
N,M = map(int,input().split())

board = []
people = []
shop = []
for i in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            people.append([i+1,j+1])
        elif board[i][j] == 2:
            shop.append([i+1,j+1])

brute = []
for b in range(len(shop)):
    if b < M:
        brute.append(0)
    else:
        brute.append(1)

print(brute)

k = 0
small = 1e9

n = list(permutations(brute))

for permution in n:
    total = 0
    for p in people:
        tmp = 1e9
        for i in range(len(shop)):
            if permution[i] == 0:
                continue
            chicken = abs(shop[i][0] - p[0]) + abs(shop[i][1] - p[1])
            tmp = min(tmp, chicken)
            total += tmp
        small = min(small,total)

print(small)

