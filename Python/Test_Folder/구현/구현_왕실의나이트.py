# 왕실의 나이트 
# 8가지 방향 돌아보면서 갈 수 있으면 카운트
# 아니면 continue
spot = input()
x = int(spot[1])
y = int(ord(spot[0])) - int(ord('a')) + 1

step = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]


cnt = 0
for i in step:
    nx = x + i[0]
    ny = y + i[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)
