# 효율적인 화폐 구성

n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] *(m+1)

d[0] = 0
for i in range(n): # i는 각각의 화폐단위를 의미
    for j in range(array[i], m+1): # j는 각각의 금액을 의미
        if d[j-array[i]] != 10001:
            d[j] = min(d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])