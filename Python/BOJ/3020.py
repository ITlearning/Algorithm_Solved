# 개똥벌레

n,h = map(int,input().split())

# 석순
stalagmite = [0] * h

# 종유석
stalactite = [0] * h

for i in range(0, n):
    num = int(input())
    if i % 2 == 0:
        stalactite[num-1] += 1
    else:
        stalagmite[num-1] += 1

for i in range(h-1, 0, -1):
    stalagmite[i-1] +=  stalagmite[i]
    stalactite[i-1] += stalactite[i]

result = 9999999999
answer = 0

for i in range(0,h):
    tmp = stalactite[i] + stalagmite[h - 1 - i]
    if tmp < result:
        result = tmp
        answer = 0
    
    if tmp == result:
        answer += 1

print(result , end=" ")
print(answer)

# https://ddggblog.tistory.com/153