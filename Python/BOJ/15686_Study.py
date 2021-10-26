# 치킨 배달
from itertools import combinations

n,m = map(int,input().split())

board = []
people = []
shop = []

for _ in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            people.append([i+1,j+1])
        elif board[i][j] == 2:
            shop.append([i+1, j+1])

small = []

brutes = list(combinations(shop, m))

for brute in brutes:
    total = 0
    for p in people:
        tmp = []
        #print(brute)
        for b in brute:
            tmp.append(abs(b[0]-p[0]) + abs(b[1]-p[1]))
        tmp.sort()
        total += tmp[0]
    #print("total", total)
    small.append(total)

small.sort()
print(small[0])