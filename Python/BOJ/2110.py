# 공유기 설치
import sys
input = sys.stdin.readline

n,c = map(int,input().split())

board = []

# 집의 좌표 입력받아서 board에 추가
for _ in range(n):
    num = int(input())
    board.append(num)
# 좌표 정렬
board.sort()

# 이분탐색 돌며
def binary_search(start,end):
    global answer
    while start <= end:
        mid = (start + end) // 2
        select = board[0] # 제일 작은 좌표
        count = 1

        for i in range(1,len(board)):
            # for문을 돌면서 중간값과 선택한 좌표의 보다 크면
            if board[i] >= mid + select:
                # 카운트 +1 하고 선택한 좌표수 갱신
                count += 1
                select = board[i]

        # 입력받은 공유기 개수보다 많거나 같을 경우
        if count >= c:
            # 답 도출
            answer = mid
            start = mid + 1
        else: # 아닐경우
            # end 갱신
            end = mid - 1


answer = 0
start = 1                  # 1로 세팅
end = board[-1] - board[0] # 좌표가 제일 큰것과 작은거 빼줌
binary_search(start,end)

print(answer)