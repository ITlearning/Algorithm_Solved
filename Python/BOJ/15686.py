# 치킨 배달
from itertools import combinations
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

k = 0
small = []

brute = list(combinations(shop,M))

for permution in brute:
    total = 0
    for p in people:
        tmp = []
        for i in permution:
            tmp.append(abs(i[0]-p[0]) + abs(i[1]-p[1]))
        tmp.sort()
        total += tmp[0]
    small.append(total)

small.sort()
print(small[0])

