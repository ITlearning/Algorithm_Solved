import sys
input = sys.stdin.readline
H, W = map(int,input().split())
block = list(map(int,input().split()))
answer = 0
 
for i in range(1, W-1):
    left = max(block[ :i])
    right = max(block[i+1: ])
    m = min(left, right)

    print(block[ :i], block[i+1: ])
    # 좌우의 블럭 높이의 최댓값 중 작은 값이 현재 블록보다 크다면
    # 반대쪽 값도 그 블럭보다 크다. 따라서 작은 값 - 현재블럭 높이 만큼 ans에 저장.
    if m > block[i]:
        answer += m - block[i]
 
print(answer)