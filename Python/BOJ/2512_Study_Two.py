# 예산
t = int(input())

board = list(map(int,input().split()))

max_num = int(input())

start = 0
end = max(board)
answer = 0
while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in board:
        if mid <= i:
            total += mid
        else:
            total += i
    
    if total <= max_num:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)