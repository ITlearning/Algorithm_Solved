# 접두사 찾기
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

board = []
match = []

answer = 0
def binary_search(start, end, text):
    global answer
    t = False
    while start <= end:
        mid = (start + end) // 2
        if str(text).startswith(match[mid]):
            answer += 1
            break
        
        if text[0] < match[mid][0]:
            end = mid - 1
        else:
            start = mid + 1

        
            


for _ in range(n):
    board.append(input().strip())

for _ in range(m):
    match.append(input().strip())

match.sort()

print(match)

for i in board:
    binary_search(1,len(match),i)

print(answer)