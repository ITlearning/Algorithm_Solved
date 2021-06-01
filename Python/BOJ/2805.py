n,m = list(map(int,input().split()))
board = list(map(int,input().split()))

board.sort()
start = 0
end = board[-1]
result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    total = sum([i-mid if i > mid else 0 for i in board])
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
