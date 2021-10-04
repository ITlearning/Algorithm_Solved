# 창고 다각형
import sys
input = sys.stdin.readline

n = int(input())

board = [0] * (1001)

max_number = -1
end_index = 0
max_index = 0
for i in range(n):
    l,h = map(int,input().split())
    if max_number < h:
        max_number = h
        max_index = l
    if end_index < l:
        end_index = l
    board[l] = h

left_max = -1
left_total = 0
for i in range(max_index+1):
    if left_max < board[i]:
        left_max = board[i]
        left_total += left_max
    else:
        left_total += left_max

right_max = -1
right_total = 0
for j in range(end_index, max_index, -1):
    if right_max < board[j]:
        right_max = board[j]
        right_total += right_max
    else:
        right_total += right_max

print(left_total + right_total)