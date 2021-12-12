# 빈도 정렬

board = {}

n, max_num = map(int,input().split())
input_numbers = list(map(int,input().split()))


for index, number in enumerate(input_numbers):
    if number in board:
        board[number][1] += 1
    else:
        board[number] = [index+1, 1]

board = sorted(board.items(), key=lambda x : (-x[1][1], x[1][0]))

for item in board:
    print((str(item[0])+" ") * item[1][1] , end="")