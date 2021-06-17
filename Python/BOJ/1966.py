# 프린터 큐 
import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
while t != 0:
    print_list, find_index = map(int, input().split())
    board = list(map(int,input().split()))
    plus = []
    index = 0
    cnt = 0
    for i in board:
        plus.append([index, i])
        index += 1
    while True:
        big = max(plus, key=lambda x: x[1])
        tmp = plus[0]
        if tmp[1] == big[1]:
            if tmp[0] == find_index:
                cnt += 1
                print(cnt)
                break
            else:
                plus.pop(0)
                cnt += 1
        elif tmp[1] < big[1]:
            plus.pop(0)
            plus.append(tmp)

    t -= 1