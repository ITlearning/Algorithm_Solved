# A -> B
from collections import deque
a,b = map(int,input().split())
inf = 1e9

q = deque()
q.append([a,1])
# 다 돌았는지 못돌았는지 체크하는 bool
t = True
# 횟수
c = 0

while q:
    x,cnt = q.popleft()
    # 입력받은 수와 현재 수랑 같으면 출력하고 중지
    if x == b:
        print(cnt)
        t = False
        break

    # 먼저 *2 가능하면 덱에 추가
    if x*2 < inf:
        q.append([x*2, cnt+1])
    # 1 추가해서 가능하면 덱에 추가
    tmp = str(x)+"1"
    if int(tmp) < inf:
        q.append([int(tmp), cnt+1])

    c += 1

# 그게 아니면 -1 출력
if t:
    print(-1)