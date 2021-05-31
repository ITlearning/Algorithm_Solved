# 떡볶이 떡 만들기
n,m = list(map(int,input().split()))
board = list(map(int,input().split()))
start = 0
end = max(board)
print(end)
result = 0
while start <= end :
    total = 0
    mid = (start + end) // 2
    for x in board:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else :
        result = mid
        start = mid + 1

print(result)