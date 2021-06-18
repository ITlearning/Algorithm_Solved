# 이진수

import sys
input = sys.stdin.readline

t = int(input())
while t != 0:
    num = int(input())

    tmp = list(format(num, 'b'))

    cnt = 0
    for i in range(len(tmp)-1,-1,-1):
        if tmp[i] == '1':
            print(cnt, end=' ')
        cnt += 1
    t -= 1