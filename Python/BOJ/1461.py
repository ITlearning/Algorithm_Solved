# 도서관

n,m = map(int,input().split())

board = list(map(int,input().split()))
minus = []
plus = []
index = 0
for i in board:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

big_number = 0
for i in board:
    if abs(i) > abs(big_number):
        big_number = i

plus.sort(reverse=True)
minus.sort()
total = []

for i in range(0, len(minus), m):
    if minus[i] != big_number:
        total.append(minus[i])

for j in range(0, len(plus), m):
    if plus[j] != big_number:
        total.append(plus[j])

answer = abs(big_number)
for num in total:
    answer += abs(num*2)

print(answer)
