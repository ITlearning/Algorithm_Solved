# 제곱수의 합
import sys
input = sys.stdin.readline

n = int(input())
# DP용 리스트
d = [0] * 100001

for i in range(1,n + 1):
    d[i] = i
    for j in range(2,i + 1):
        if j*j <= i:
            d[i] = min(d[i], d[i - (j * j)] + 1)

print(d[n])

# d[0] = 0 
# d[1] = 1^2 -> 1개
# d[2] = 1^2, 1^2 -> 2개
# d[3] = 1^2, 1^2, 1^2 -> 3개
# d[4] = (1^2, 1^2, 1^2, 1^2), (2^2) -> 4개, 1개 -> 1개
# 구성되어있는 개수 중 최소의 개수를 파악하는 것이니,
# 점화식은 min(d[i], d[i - (j*j)]+ 1)
# 뒤에 +1은 j의 제곱수의 대한 개수
