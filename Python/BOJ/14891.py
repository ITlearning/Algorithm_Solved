# 톱니바퀴
gear = []

for _ in range(4):
    tmp = map(int,input())
    gear.append(list(tmp))

k = map(int,input())

for i in range(k):
    number, direction = map(int,input().split())
    