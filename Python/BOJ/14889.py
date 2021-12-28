# 스타트와 링크
from itertools import combinations
n = int(input())
board = []
check = [i for i in range(n)]

for _ in range(n):
    board.append(list(map(int,input().split())))

answer = 99999999999

for start_combi in combinations(check, n//2):
    start = 0
    link = 0
    link_combi = list(set(check)-set(start_combi))

    for s in combinations(start_combi, 2):
        start += board[s[0]][s[1]]
        start += board[s[1]][s[0]]

    for l in combinations(link_combi, 2):
        link += board[l[0]][l[1]]
        link += board[l[1]][l[0]]
    
    answer = min(answer, abs(start - link))

print(answer)