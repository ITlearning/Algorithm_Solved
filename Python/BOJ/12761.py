# 돌다리 
from collections import deque
A, B, dong_gyu, jumi = map(int,input().split())

# 돌 다리 거리 최대수로 초기화
rock_bridge = [999999999] * (100001)

q = deque()
# 덱 시작에 동규 위치 추가
q.append(dong_gyu)

# 동규 위치의 거리는 1로 설정
rock_bridge[dong_gyu] = 1

while q:
    x = q.popleft()
    # 뽑은 위치가 주미의 위치라면
    if x == jumi:
        # 현재 거리에서 1 빼고 출력
        print(rock_bridge[x]-1)
        break
    # 그게 아니면 모든 경우의 수 확인
    for i in (x-1, x+1, x+A, x+B, x*A, x*B, x-A, x-B):
        if 0 < i < 100001:
            # 이동한게 아니라면
            if rock_bridge[i] == 999999999:
                # 이동 시키고 +1
                rock_bridge[i] = rock_bridge[x] + 1
                q.append(i)