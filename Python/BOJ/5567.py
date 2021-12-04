# 결혼식
from collections import deque

n = int(input())
m = int(input())

board = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    # 두 위치에 친구 추가 
    board[a].append(b)
    board[b].append(a)
# 위치 최대 수로 초기화
distance = [99999999]*(n+1)
q = deque()

# 시작 위치 0으로 설정
q.append(1)
distance[1] = 0

# 덱 시작
while q:
    x = q.popleft()
    # 덱에서 뽑은 친구의 리스트를 확인
    for i in board[x]:
        # 아직 이동한 거리가 아니라면
        if distance[i] > distance[x]:
            # 확인된 친구의 거리에 상태 업데이트 (+1)
            distance[i] = distance[x] + 1
            # 친구 추가
            q.append(i)

answer_cnt = 0
for an in distance:
    # 0은 애초에 친구 아닌거고, 3이면 친구의, 친구의, 친구가 되는 거니 친구라 할 수 없음
    if an > 0 and an < 3:
        answer_cnt += 1

print(answer_cnt)

