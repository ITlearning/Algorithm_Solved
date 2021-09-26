# 용돈 관리

n,m = map(int,input().split())
board = []
answer = 0

def binary_search(start,end):
    global answer
    while start <= end:
        mid = (start+end) // 2
        cnt = 1
        total = mid # 미드값이 인출할 금액
        for i in range(n):
            if total < board[i]: # 만일 가지고 있는 돈 보다 큰 금액이 나올 경우
                cnt += 1         # 카운트 증가시키고 다시 돈 뽑음
                total = mid
            total -= board[i] # 그거는 그거대로 계산은 계산대로

        # 횟수가 초과 됐거나, 인출한 금액이 제일 큰수까지 커버를 못한다면    
        if cnt > m or mid < max(board):
            start = mid + 1
        # 적합하면
        else:
            end = mid - 1
            answer = mid


for i in range(n):
    tmp = int(input())
    board.append(tmp)

start = min(board) # 입력 받은 수 중 가장 작은 수
end = sum(board)   # 합계

binary_search(start,end)

print(answer)