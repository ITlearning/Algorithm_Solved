# 상자넣기

n = int(input())

board = list(map(int,input().split()))

dp = [1 for _ in range(n+1)]

# 이중 for문을 돌려서
# 현재 인덱스의 숫자가
# 클 경우에만 카운트를 진행하여
# 제일 큰 수를 찾으면 되는 문제
for i in range(1,n):
    for j in range(i):
        if board[i] > board[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

