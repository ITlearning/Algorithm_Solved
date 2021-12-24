# 크리스마스 선물
import heapq

n = int(input())
q = []
for _ in range(n):
    a = list(map(int,input().split()))
    
    if a[0] != 0:
        numbers = a[1:]
        for number in numbers:
            heapq.heappush(q, -number)
    else:
        if q:
            print_num = heapq.heappop(q)
            print(-print_num)
        else:
            print(-1)
