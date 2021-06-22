# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
N,K = map(int,input().split())
cnt = 0
while N != 1:
    if N % K == 0:
        N //= K
        cnt += 1
        continue
    N -= 1
    cnt += 1
    

print(cnt)