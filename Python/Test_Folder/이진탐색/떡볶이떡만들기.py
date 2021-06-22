import sys
input = sys.stdin.readline
N,M = map(int,input().split())

board = list(map(int,input().split()))

start = 0
end = max(board)
result = 0
def binary_search(start, end, target):
    global result 
    result = 0
    
    while start <= end:
        print(start, end)
        mid = (start+end) // 2
        tmp = 0
        for x in board:
            if x > mid:
                tmp += x - mid
        if tmp < M:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
binary_search(start, end, M)
print(result)