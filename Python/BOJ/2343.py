# 기타 레슨

n,m = map(int,input().split())

board = list(map(int,input().split()))

answer = 999999999999

def binary_search(start, end):
    global answer
    while start <= end:
        mid = (start+end) // 2
        cnt = 0
        total = 0
        for i in range(n):
            # 전체 리스트를 돌면서 mid 값보다 클 경우
            if total + board[i] > mid:
                # 카운트 +1 증가시키고
                cnt += 1
                # 지금까지 더해놓은 분 초기화
                total = 0
            # 그거와 상관없이 계속 더하던건 더함
            total += board[i]
        
        # total 이 0 이 아닐경우
        if total:
            cnt += 1
        
        # 그렇게 해서 나온 개수가 입력받은 m보다 클 경우에는
        if cnt > m:
            # start 값 갱신
            start = mid + 1
        else:
            # 그게 아니면, 답에 최소 분 값 저장
            answer = min(answer, mid)
            end = mid - 1


start = max(board) # 입력받은 블루레이 크기 중 가장 큰 블루레이
end = sum(board)   # 입력받은 블루레이 총 합
# start = 9, end = 45

binary_search(start, end)

print(answer)