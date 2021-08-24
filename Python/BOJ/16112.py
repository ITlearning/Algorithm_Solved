# 5차 전직
import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
answer = []
board = list(map(int,input().split()))

# 최소힙으로 입력 받은 수 정리
for i in board:
    heapq.heappush(answer, i)

total = 0 # 전체 값
cur = 0 # 인덱스 숫자 카운트

# 돌면서 인덱스 수 만큼 곱해준다.
# 어짜피 로직상, 작은 것부터 뽑아서 그 인덱스 수에 맞게 곱해주면 답이 나온다.

# ex) 100 * 0 , 200 * 1, 300*2 = 800
for i in range(n):
    tmp = heapq.heappop(answer)
    total += tmp*cur
    if cur < k:
        cur += 1

print(total)