# 정수 삼각형
import sys
input = sys.stdin.readline
n = int(input())

t = []
for _ in range(n):
    t.append(list(map(int, input().split())))

k = 2
for i in range(1,n):
    for j in range(k):
        if j == 0: # 완전히 왼쪽일 경우에는 그 위에 것이랑 더하기
            t[i][j] = t[i][j] + t[i-1][j]
        elif i == j: # 완전히 오른쪽일 경우에는 그 위에 것이랑 더하기
            t[i][j] = t[i][j] + t[i-1][j-1]
        else: # 그게 아니고 영향을 2개 받는 위치일 경우, 위에 숫자 중 더 큰걸로 더하기
            t[i][j] = max(t[i-1][j-1], t[i-1][j]) + t[i][j]
    k += 1
# 마지막 줄에는 각자 라인을 타고 내려온 값들이 있는데, 그 값들 중에 가장 높은걸로 출력
print(max(t[n-1]))