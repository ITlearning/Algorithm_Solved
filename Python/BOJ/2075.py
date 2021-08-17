# N 번째 큰 수
import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
que = PriorityQueue()
for i in range(n*n):
    j = int(input().rstrip())
    if que.qsize() >= 5:
        que.get() 
    que.put(j)

print(que.get())
