# 수들의 합
import sys
input = sys.stdin.readline
s = int(input())
tmp = 0
cur = 0
while tmp < s:
    cur += 1
    tmp += cur

if tmp == s:
    print(cur)
else:
    print(cur - 1)
