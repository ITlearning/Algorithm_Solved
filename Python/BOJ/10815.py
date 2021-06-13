# 숫자 카드
import sys
input = sys.stdin.readline
n = int(input())
boardOne = list(map(int,input().split()))


# 일단 작은 순서대로 정렬을 해준다.
boardOne.sort()

# 이분 탐색을 돌며 해당 수가 나오면 1, 아니면 0을 리턴하게 된다.
# 애초에 수들을 정렬 해놓았기 때문에, 중간부터 수가 만일 크면 오른쪽
# 작으면 왼쪽으로만 가면 되기때문에 시간 복잡도가 많이 줄어든다.
def binary_search(num):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end) // 2
        if boardOne[mid] == num:
            return 1
        elif boardOne[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

y = int(input())

for num in list(map(int,input().split())):
    print(binary_search(num), end=' ')