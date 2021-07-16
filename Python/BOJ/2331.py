# 반복수열
import sys
input = sys.stdin.readline

a,p = map(int, input().split())

next = a+1

D = []
tmp = a
while True:
    t = str(tmp)
    total = 0
    for i in t:
        total += pow(int(i), p)
    if total not in D:
        D.append(total)
    else:
        tmp = total
        break
    tmp = total

print(tmp)