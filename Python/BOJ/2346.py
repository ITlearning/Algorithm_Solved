# 풍선 터뜨리기
from collections import deque
n = int(input())

board = list(map(int,input().split()))
result = []
q = deque()

for i in range(n):
    q.append([i+1, board[i]])

while q:
    t, num = q.popleft()
    result.append(t)
    
    if num-1 > 0:
        for _ in range(abs(num-1)):
            q.rotate(-1)
    elif num < 0:
        for _ in range(abs(num)):
            q.rotate(1)
    
print(*result)
    