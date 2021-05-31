# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right
# 값이[leftValue, rightValue]인 데이터의 개수를 반환하는 함수
def count_by_range(a, leftValue, rightValue) :
    rightIndex = bisect_right(a,rightValue)
    leftIndex = bisect_left(a,leftValue)

    return rightIndex - leftIndex


n,m = list(map(int,input().split()))
board = list(map(int,input().split()))

if count_by_range(board,m,m) == 0 :
    print("-1")
else:
    print(count_by_range(board,m,m))