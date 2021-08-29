# K번째 수
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 1, k
answer = 0
while start <= end:
    mid = (start+end) // 2
    tmp = 0

    # A[i][j] 에서 i의 행에 속한 숫자들은 i*j이므로 모두 i의 배수.
    # 각 행과 mid를 나눌경우, 그 행에 mid 보다 작은 수의 개수가 나옴.
    # 그 개수와 n의 수를 비교해 더 작은 수 기입.
    # 그렇게 하면 mid 수보다 작은 숫자들의 개수가 나옴.
    for i in range(1,n+1):
        tmp += min(mid//i, n)
        print(mid//i, n)
    print("tmp:",tmp)
    if tmp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)

# https://codingsmu.tistory.com/79