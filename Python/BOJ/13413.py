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
    check_board = []
    check_match = []
    for i in range(len(board)):
        if board[i] != match[i]:
            check_board.append(board[i])
            check_match.append(match[i])
    check_match.sort()
    check_board.sort()

    for i in range(len(check_board)):
        if check_board[i] == check_match[i]:
            cnt += 0.5
        else:
            cnt += 1
    print(int(cnt))
    T -= 1

