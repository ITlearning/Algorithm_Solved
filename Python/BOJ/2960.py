# 에라토스테네스의 체
n,k = map(int,input().split())

board = [True] * (n+1)
cnt = 0
# 2 부터 n까지 돌리기
for i in range(2, len(board)+1):
    # 돌리면서 i 간격만큼 돌리기
    for j in range(i, n+1, i):
        # Bool 값이 True 라면
        if board[j] == True:
            # False 처리 후 카운트 증가
            board[j] = False
            cnt += 1
            # 그러다가 카운트 값이 입력받은 K 랑 같아지면 출력 후 종료
            if cnt == k:
                print(j)
                break