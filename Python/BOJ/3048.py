# 개미
left, right = map(int,input().split())

left_board = list(input())
right_board = list(input())

dic = {}

for text in left_board:
    dic[text] = 0

for text in right_board:
    dic[text] = 1

t = int(input())
left_board.reverse()
left_board.extend(right_board)

for _ in range(t):
    index = 0
    while index < len(left_board)-1:
        if dic[left_board[index]] == 0 and dic[left_board[index+1]] == 1:
            left_board[index] , left_board[index+1] = left_board[index+1], left_board[index]
            index += 1
        index += 1

print("".join(left_board))