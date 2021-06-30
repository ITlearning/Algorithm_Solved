# 패션왕 신해빈
from collections import Counter
import sys
input = sys.stdin.readline
T = int(input())
while T != 0:
    N = int(input())
    answer = []
    for i in range(N):
        item, using = map(str,input().split())
        answer.append(using)
    
    result = Counter(answer)
    total = 1
    for i in result.values():
        total *= i+1
    print(total - 1)
    T -= 1
