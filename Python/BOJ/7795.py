# 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

n = int(input())
board_a = []
board_b = []

def binary_search(b,a):
    start = 0
    end = len(b)-1
    total = -1
    while start <= end:
        mid = (start+end)//2
        if b[mid] < a:
            total = mid
            start = mid+1
        else:
            end = mid-1
    return total


while True:
    if n == 0:
        break
    a_len,b_len = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    cnt = 0
    for num in a:
        cnt += binary_search(b,num) + 1

    print(cnt)
    n -= 1