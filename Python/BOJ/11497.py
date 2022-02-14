# 통나무 건너뛰기
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

while t != 0:
    left = deque()
    right = deque()
    plus = deque()
    result = []
    n = int(input())
    board = list(map(int, input().split()))
    # 입력받은 리스트 반대로 정렬
    board.sort(reverse=True)
    print(board)

    # 첫 통나무와 마지막 통나무가 인접해있다라는 조건이 있기때문에
    # 그냥 정렬로는 안되고, 두개의 리스트를 만들어
    # 가장 큰 수를 기점으로 양쪽에 점점 작게 배치를 하면
    # 최소수를 유지하면서 제일 큰 높이 차를 만들어낼 수 있다.
    while len(board) > 1:
        left.append(board.pop())
        right.appendleft(board.pop())
    
    if len(board) == 1:
        left.append(board.pop())

    
    print("left", left)
    print("right", right)

    plus = left + right
    for i in range(len(plus)-1):
        result.append(abs(plus[i] - plus[i+1]))
    
    print(max(result))
    t -= 1
