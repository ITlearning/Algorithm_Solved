# 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

# 방문 여부 체크 리스트
dist = [0] * (100001)
# 횟수
time = 0

q = deque()

# 수빈이 시작 위치 일단 넣기
q.append([n,0])
total = 0
while q:
    x, time = q.popleft()

    # 수빈이의 위치가 동생의 위치와 같을 경우
    if x == k:
        print(time)
        break
    
    # 먼저 2배일때 이동을 체크 해준다.
    # 대신 시간 증가는 X
    if x*2 >= 0 and x*2 < 100001:
        if dist[x*2] == 0:
            dist[x*2] = 1
            q.append([x*2,time])
        
    # 그리고 나서 나머지 앞 뒤 확인을 거친다.
    for i in (x-1, x+1):
        if i >= 100001 or i < 0:
                continue
        if dist[i] == 0:
            dist[i] = 1
            q.append([i, time+1])
