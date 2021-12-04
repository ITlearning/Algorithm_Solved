# 안테나

n = int(input())

board = list(map(int,input().split()))
max_len = max(board)

start = 0
end = max_len
answer = 999999999999

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in board:
        tmp += abs(i - mid)

    if tmp < answer:
        answer = tmp
        start += mid + 1
    else:
        end = mid - 1

print(answer)