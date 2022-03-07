# 용액

n = int(input())

board = list(map(int,input().split()))

start = 0
end = n-1
result = 999999999999999999

# 왼쪽 결과
result_left = 0
# 오른쪽 결과
result_right = 0

# 투 포인터를 이용하여 양쪽의 포인터가 만날때까지 계속 돌려주면 된다.

while start < end:
    # 합이 음수라면
    if board[start] + board[end] < 0:
        if abs(board[start] + board[end]) < result:
            result = abs(board[start] + board[end])
            result_left = board[start]
            result_right = board[end]
        # 왼쪽 포인터 움직이기
        start += 1
    # 합이 양수라면
    elif board[start] + board[end] > 0:
        # 절댓값으로 변환해서 그 값이 더 작다면
        if abs(board[start] + board[end]) < result:
            # 갱신
            result = abs(board[start] + board[end])
            result_left = board[start]
            result_right = board[end]
        # 오른쪽 포인터 움직이기
        end -= 1
    # 0이 나오면
    elif board[start] + board[end] == 0:
        # 갱신하고 중지
        result = abs(board[start] + board[end])
        result_left = board[start]
        result_right = board[end]
        break

print(result_left, result_right)
