# 문자열

# 계속 틀린거
"""
import sys
input = sys.stdin.readline
# sys 를 사용하면 뒤에 \n 이 들어가서 아마도 문제가 되는듯 하다.
# 이걸 계속 알면서도 삽질했다 하;

a,b = input().split()

total = 1e9
cur = len(b)-len(a)
for i in range(cur+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt += 1
    total = min(total, cnt)

print(total)
"""

# 정답
a,b = input().split()

total = 1e9
cur = len(b)-len(a)
for i in range(cur+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt += 1
    total = min(total, cnt)

print(total)
