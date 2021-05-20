n = int(input())

num = input().split()

for i in range(len(num)) :
    num[i] = int(num[i])
v = int(input())
cnt = 0
for i in num :
    if i == v :
        cnt += 1

print(cnt)