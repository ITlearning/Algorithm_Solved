# A -> B
from collections import deque

a,b = map(int,input().split())
inf = 1e9
q = deque()
q.append([a,1])
t = True
c = 0
while q:
    #print(q)
    x,cnt = q.popleft()
    if x == b:
        print(cnt)
        t = False
        break
    if x*2 < inf:
        q.append([x*2, cnt+1])
    tmp = str(x)+"1"
    if int(tmp) < inf:
        q.append([int(tmp), cnt+1])

    c += 1

if t:
    print(-1)