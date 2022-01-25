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
