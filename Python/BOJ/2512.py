# 예산
import sys
input = sys.stdin.readline

t = int(input())

board = list(map(int,input().split()))
topic = int(input())
start = 0
end = topic
answer = 0
if sum(board) <= topic:
    answer = max(board)
else:
    while start <= end:
        mid = (start+end) // 2
        result = 0
        for i in board:
            if i > mid:
                result += mid
            else:
                result += i
        if result <= topic:
            answer = mid
            start = mid + 1
        elif result > topic:
            end = mid - 1

print(answer)