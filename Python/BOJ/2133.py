# 타일 채우기

n = int(input())

# 애초에 타일의 넓이는 2짜리이기에
# 벽의 길이가 홀수일 경우에는 만들어질 수가 없다.
dp = [0] * 31
dp[0] = 1
dp[2] = 3

if n % 2 != 0:
    print(0)
else:
    for i in range(4,n+1):
        dp[i] = dp[i-2] * 3
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2

    print(dp[n])