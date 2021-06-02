# 금광 
t = int(input())

for _ in range(t) :
    n,m = list(map(int,input().split()))
    board = list(map(int,input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(board[index:index+m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1: left_down = 0
            else: left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            # 이 셋중에서 제일 큰것과 현재 dp와 합쳐서 더하기
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0

    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)