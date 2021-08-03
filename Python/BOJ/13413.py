# 오셀로 재배치
import sys
input = sys.stdin.readline

T = int(input())

while T > 0:
    N = int(input())
    text = input().rstrip()
    board = list(text)
    text = input().rstrip()
    match = list(text)
    cnt = 0
    tri = True
    # 1. 배치된 말 중 임의의 2개의 말을 골라 서로의 위치를 바꾼다.
    t = False
    for i in range(len(board)-1):
        if board[i] != board[i+1]:
            if board[i] != match[i]:
                board[i], board[i+1] = board[i+1], board[i]
            else:
                
    print(cnt)
    T -= 1

