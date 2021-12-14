# 포도주 시식

n = int(input())

wine = [0 for _ in range(n+1)]

for i in range(1, n+1):
    wine[i] = int(input())

dp = [0 for _ in range(n+1)]

# 와인의 개수가 3개 이하면
if n < 3:
    # 그냥 더하고 출력
    print(sum(wine))
# 그게 아니면
else:
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    # i + i-2 , i + i-1, i를 안먹었을 경우
    dp[3] = max(wine[3]+wine[1], wine[3]+wine[2], dp[2])
    for i in range(4,n+1):
        # 지금 인덱스의 와인 + i-2 까지 먹은 양, 
        # 지금 와인 + 이전 와인 + (3개 연속으로 못먹는다고 했으니) 3개 연속 뒤에 까지 먹은 양,
        # 지금 인덱스의 와인을 안먹은 경우,
        dp[i] = max(wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3], dp[i-1])

    print(max(dp))