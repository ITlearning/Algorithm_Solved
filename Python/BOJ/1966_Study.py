# 프린터 큐
from collections import deque

t = int(input())
for i in range(t):
    document_num, find_index = map(int,input().split())
    board = list(map(int,input().split()))
    q = deque()
    for i,number in enumerate(board):
        q.append([number, i])
    max_num = max(q, key=lambda x: x[0])
    cnt = 1
    while True:
        # 지금 가장 큰 수부터 뽑을라고 하니까 조건
        if q[0][0] == max_num[0]:
            if q[0][1] == find_index:
                print(cnt)
                break
            cnt += 1
            q.popleft()
            max_num = max(q, key=lambda x: x[0])
            continue
        else:
            q.append(q.popleft())



