# 11726 2xN 타일링

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 2
for i in range(3,n+1):
    d[i] = (d[i-1] + d[i-2]) % 10007

print(d[n])

# 점화식을 세우는게 좀 걸렸다.
# 이 문제의 점화식은 answer: a(n-1)+a(n-2)이다.