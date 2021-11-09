# 예산
t = int(input())

board = list(map(int,input().split()))

max_num = int(input())

start = 0 # 시작 0
end = max(board) # 끝 board에서 가장 큰 수
answer = 0

while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in board:
        # mid 값이 board의 숫자보다 작거나 같으면
        if mid <= i:
            # mid 값 추가
            total += mid
        else:
            # 그거 아니면 board 값 추가
            total += i
    # 비교
    if total <= max_num:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)