# 개똥벌레

n,h = map(int,input().split())

# 석순
stalagmite = [0] * h

# 종유석
stalactite = [0] * h

# 1. for문을 돌며 석순과 종유석에 따라서 (짝수,홀수) 해당되는 인덱스의 리스트 숫자를 증가시켜준다.
for i in range(0, n):
    num = int(input())
    if i % 2 == 0:
        stalactite[num-1] += 1
    else:
        stalagmite[num-1] += 1

# 2. 그리고 난 뒤 뒤에서부터 전체 종유석, 석순의 숫자를 더해준다. (누적합을 구함)
for i in range(h-1, 0, -1):
    stalagmite[i-1] +=  stalagmite[i]
    stalactite[i-1] += stalactite[i]

result = 9999999999
answer = 0

# 3. 그리고 누적합이 같은 구간끼리 더해서 답을 도출한다.
for i in range(0,h):
    tmp = stalactite[i] + stalagmite[h - 1 - i]
    
    if tmp < result:
        result = tmp
        answer = 0
    
    if tmp == result:
        answer += 1

print(result , end=" ")
print(answer)

