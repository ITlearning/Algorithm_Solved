# 5차 전직
import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
t = list(map(int,input().split()))
board = []
for i in t:
    heapq.heappush(board,-i)

total = []

num = 0

for i in range(n):
    tmp = heapq.heappop(board)
    if len(board) > k-1:
        num += num
        num += abs(tmp)
        #total.append(tmp)

print(num)