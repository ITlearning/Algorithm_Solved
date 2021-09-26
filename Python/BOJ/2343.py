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
            if total + board[i] > mid:
                cnt += 1
                total = 0
            total += board[i]
        
        if total:
            cnt += 1
        
        if cnt > m:
            start = mid + 1
        else:
            answer = min(answer, mid)
            end = mid - 1


start = max(board)
end = sum(board)

binary_search(start, end)

print(answer)