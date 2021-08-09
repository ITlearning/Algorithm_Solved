# 패션왕 신혜빈
from collections import Counter
T = int(input())
while T > 0:
    board = []
    N = int(input())
    total = N
    for i in range(N):
        stuff, category = map(str,input().split())
        board.append(category)

    result = Counter(board)
    total = 1
    for i in result.values():
        total *= i+1
    print(total - 1)
    T -= 1