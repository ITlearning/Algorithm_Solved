# 프린터 큐
from collections import deque

t = int(input())
for i in range(t):
    # 문서 숫자, 찾을 수
    document_num, find_index = map(int,input().split())

    board = list(map(int,input().split()))
    q = deque()

    # 인덱스랑 입력받은 문서 뽑아서 덱에 같이 넣어줌
    for i,number in enumerate(board):
        q.append([number, i])
    # 제일 큰 숫자 뽑아내기
    max_num = max(q, key=lambda x: x[0])
    cnt = 1
    while True:
        # 지금 가장 큰 수부터 뽑을라고 하니 조건 생성
        # 지금 가장 왼쪽의 수가 제일 큰 수면 
        if q[0][0] == max_num[0]:
            # 근데 그 수가 또 우리가 찾을 인덱스와 같다면?
            if q[0][1] == find_index:
                print(cnt)
                break
            # 그거 아니면 카운트 증가시키고 숫자 뽑아내기
            cnt += 1
            q.popleft()
            # 그리고 최신으로 제일 큰 수 갱신
            max_num = max(q, key=lambda x: x[0])
        else:
            # 제일 큰 수 아니면 뒤로 넘기기
            q.append(q.popleft())