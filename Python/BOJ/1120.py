# 문자열
import sys
input = sys.stdin.readline

a,b = input().split()

total = 999999999999
cur = len(b)-len(a)
for i in range(cur+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt += 1
    total = min(total, cnt)

print(total)
