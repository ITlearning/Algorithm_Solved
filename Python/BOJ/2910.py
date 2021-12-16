# 빈도 정렬
board = {}

n, max_num = map(int,input().split())
input_numbers = list(map(int,input().split()))

# 딕셔너리에 숫자와 횟수 저장
for index, number in enumerate(input_numbers):
    if number in board:
        board[number][1] += 1
    else:
        board[number] = [index+1, 1]

# 횟수는 큰순서대로, 그게 같으면 숫자순서대로 정렬
board = sorted(board.items(), key=lambda x : (-x[1][1], x[1][0]))

# 출력
for item in board:
    print((str(item[0])+" ") * item[1][1] , end="")