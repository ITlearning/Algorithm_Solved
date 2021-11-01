# A -> B
from collections import deque

a,b = map(int,input().split())
inf = 1e9
board = [0] * (int(inf)+1)

board[a] = 1
q = deque()
q.append(b)
t = True
cnt = 0
while q:
    x = q.popleft()
    if x == a:
        print(cnt+1)
        break
    if x*2 < inf:
        board[x*2] += board[x] + 1
        q.append(x*2)
    tmp = str(x)+"1"
    if int(tmp) < inf:
        board[int(tmp)] += board[x] + 1
        q.append(int(tmp))


if t:
    print(-1)