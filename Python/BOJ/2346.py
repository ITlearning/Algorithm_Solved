# 풍선 터뜨리기
from collections import deque
n = int(input())

board = list(map(int,input().split()))
result = []
q = deque()

# 입력받은 풍선을 덱에 순서와 함께 추가
for i in range(n):
    q.append([i+1, board[i]])

# 가장 왼쪽껄 뽑는 로직으로 설정
while q:
    t, num = q.popleft()
    # 결과값에 순서 추가
    result.append(t)
    
    # 뽑은 풍선의 인덱스 이동 숫자가 양수일 경우
    if num-1 > 0:
        for _ in range(abs(num-1)):
            # 그만큼 돌리기
            q.rotate(-1)
    # 뽑은 풍선의 인덱스 이동 숫자가 음수일 경우
    elif num < 0:
        for _ in range(abs(num)):
            # 그만큼 돌리기
            q.rotate(1)
    
print(*result)
    