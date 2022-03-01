# 용액

n = int(input())

board = list(map(int,input().split()))

start = 0
end = n-1
result = 999999999999999999

result_left = 0
result_right = 0

while start < end:
    # 합이 음수라면
    if board[start] + board[end] < 0:
        if abs(board[start] + board[end]) < result:
            result = abs(board[start] + board[end])
            result_left = board[start]
            result_right = board[end]
        
        start += 1
    elif board[start] + board[end] > 0:
        if abs(board[start] + board[end]) < result:
            result = abs(board[start] + board[end])
            result_left = board[start]
            result_right = board[end]
        
        end -= 1
    elif board[start] + board[end] == 0:
        result = abs(board[start] + board[end])
        result_left = board[start]
        result_right = board[end]
        break

print(result_left, result_right)
