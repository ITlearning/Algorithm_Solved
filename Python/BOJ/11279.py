# 최대 힙
import heapq
import sys
input = sys.stdin.readline
t = int(input())
q = []
for _ in range(t):
    
    num = int(input())
    if num == 0:
        if len(q) != 0:
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,-num)