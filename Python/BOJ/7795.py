# 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

n = int(input())

# 이분탐색
def binary_search(b,a):
    start = 0
    end = len(b)-1
    total = -1 # 답이 될 변수. -1로 시작해야 답이 도출된다.
    while start <= end:
        mid = (start+end)//2
        if b[mid] < a: # 만약 중간의 수가 a보다 작다면
            total = mid # 답으로 해당 인덱스를
            start = mid+1 # 시작점을 중간에서 증가
        else: # 그게 아니면
            end = mid-1 # 끝 점을 하나 뺴줌
    return total


while n != 0:
    a_len,b_len = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    cnt = 0
    for num in a:
        cnt += binary_search(b,num) + 1

    print(cnt)
    n -= 1