# 제곱수의 합
import sys
input = sys.stdin.readline
n = int(input())

d = [0] * 100001

for i in range(1,n+1):
    d[i] = i
    for j in range(2,i+1):
        if j*j <= i:
            d[i] = min(d[i], d[i - (j*j)]+1)

print(d[n])