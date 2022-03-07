# 떡 먹는 호랑이
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 30

# 피보나치 함수를 재귀함수로 구현
def fibo(x):
    if x <= 1:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

day, items = map(int,input().split())

# 1 → 1 → 2 → 3 → 5 → 8 → 13 → . . .
# 피보나치 수열을 형성 한다고 하는데 잘 모르겠음.. 더 이해하고 한번 더 풀어보겠음..!
x = fibo(day-3)
y = fibo(day-2)

for i in range(items):
    for j in range(items):
        if (i*x) + (j*y) == items:
            if i < j:
                print(i)
                print(j)
                exit()

