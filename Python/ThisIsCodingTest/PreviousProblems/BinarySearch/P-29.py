# 공유기 설치

n,m = list(map(int,input().split()))
board = []
for _ in range(n) :
    board.append(int(input()))

board.sort()

start = 1
end = board[-1] - board[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    old = board[0]
    count = 1

    for i in range(1, len(board)):
        if board[i] >= old+mid:
            count += 1
            old = board[i]

    if count >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)


# https://assaeunji.github.io/python/2020-05-07-bj2110/