# 랜선 자르기
import sys
input = sys.stdin.readline

k,n = map(int,input().split())

board = []
for _ in range(k):
    board.append(int(input()))

answer = 0
start = 1 # 이 수를 0으로 처리 해놨을 경우에 런타임 에러(ZeroDivisionError)가 발생한다. 되도록이면 초기 설정값을 1로 설정하자.
end = max(board)
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for i in board:
        cnt += i // mid
        if cnt >= n:
            break
    
    if cnt >= n:
        answer = mid
        start = mid + 1
    elif cnt < n:
        end = mid - 1

print(answer)
