from collections import deque

n,k = map(int,input().split())

q = deque()

dist = [-1] * 200001
q.append([n,k])
while True:
    x ,y= q.popleft()
    if x == y:
        print(dist[x])
        break
    for xn in (x+1, x-1, x*2):
        print(xn)
        if xn < 0 or xn >= 200000:
            continue
        if dist[xn] == -1:
            dist[xn] = dist[x]+1
            q.append(xn)

        

