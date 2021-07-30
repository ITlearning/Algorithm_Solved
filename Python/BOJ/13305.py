# 주유소
import sys
input = sys.stdin.readline
N = int(input())
road = list(map(int,input().split()))
location = list(map(int,input().split()))

total = road[0]*location[0]
small = location[0]
tmp = 0
for i in range(1,N-1):
    # 리터당 가격이 작을 경우(원래 작다고 했던것보다)
    if location[i] < small:
        total += small*tmp
        tmp = road[i]
        small = location[i]
    else:
        tmp += road[i]

    if i == N-2:
        total += tmp*small
print(total)
