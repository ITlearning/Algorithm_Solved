# 수 찾기
import sys
input = sys.stdin.readline

n_one = int(input())
# 입력받면서 정렬
board_one = sorted(list(map(int,input().split())))

n_two = int(input())

board_two = list(map(int,input().split()))

# 이분탐색을 하면서, 원하는 숫자가 있을 경우 1, 아닐경우 0을 도출
def binary_search(num):
    start = 0
    end = n_one-1
    answer = 0
    while start <= end:
        mid = (start+end)//2
        if board_one[mid] == num:
            answer = 1
            start = mid + 1
            return answer
        elif board_one[mid] < num:
            answer = 0
            start = mid + 1
        else:
            answer = 0
            end = mid - 1
    return answer


for i in range(n_two):
    tmp = binary_search(board_two[i])
    print(tmp)