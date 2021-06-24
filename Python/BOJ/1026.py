# 보물
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

total = 0
for i in range(n):
    total += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(total)