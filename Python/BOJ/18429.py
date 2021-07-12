from itertools import permutations
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

board = list(map(int,input().split()))

tmp = permutations(board, n)
cnt = 0
for i in tmp:
    t = True
    value = 500
    for j in i:
        value -= k
        if value + j < 500:
            t = False
            break
        else:
            value += j
    if t:
        cnt += 1

print(cnt)
