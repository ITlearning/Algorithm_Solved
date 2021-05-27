# 모험가 길드

n = int(input())
board = list(map(int,input().split()))
board.sort()

count = 0
team = 0
for i in board :
    count += 1
    if count >= i :
        team += 1
        count = 0
print(team)