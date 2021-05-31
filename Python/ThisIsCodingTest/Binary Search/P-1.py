# 부품 찾기

def binary_search(array, target, start, end) :
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
nx = list(map(int,input().split()))

m = int(input())
ny = list(map(int,input().split()))

for i in ny:
    result = binary_search(nx,i,0,n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')