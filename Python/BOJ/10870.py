# 피보나치 수 5
import sys
input = sys.stdin.readline
num = int(input())
def fibo(n):
    fi = [1,1]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    for i in range(2,n):
        fi.append(fi[i-1] + fi[i-2])
    return fi[num-1]
print(fibo(num))