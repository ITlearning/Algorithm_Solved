# N 번째 큰 수
import heapq

n = int(input())
que = []

# 일단 이렇게 해서 초기 최대 개수를 정해준다.
# 그리고 첫 줄에 수를 모두 다 넣어준다.
for i in map(int,input().split()):
    heapq.heappush(que, i)

for _ in range(1,n):
    for num in map(int,input().split()):
        # 입력받은 수 하나 들어가고 ( 개수 : 6개)
        heapq.heappush(que,num)
        # 그리고 제일 작은 수 빼준다. ( 개수 : 5개)
        heapq.heappop(que)

print(heapq.heappop(que))
