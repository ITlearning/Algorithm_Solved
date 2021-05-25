# 실전문제 2
# 큰 수의 법칙

n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
bigOne = data[n-1]
bigTwo = data[n-2]

result = 0

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1)

result += (count) * bigOne
result += (m-count) * bigTwo
print(result)