# 소수 사이 수열
import sys
import math
input = sys.stdin.readline

n = 1300000
prime_bool = [False for _ in range(n+1)]

# 1. 소수 판별
for i in range(2, n):
    if prime_bool[i]: continue
    for j in range(i+i,n,i):
        prime_bool[j] = True

# 2. 소수만 따로 정리
prime = [i for i in range(2,n+1) if prime_bool[i] == False]

# 테스트 케이스
t = int(input())

def binary_search(key):
    start = 2
    end = len(prime) - 1
    while start <= end:
        mid = (start + end)//2
        if prime[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    
    return start

for _ in range(t):
    key = int(input())
    if not prime_bool[key]:
        print("0")
    else:
        index = binary_search(key)
        print(prime[index] - prime[index-1])

