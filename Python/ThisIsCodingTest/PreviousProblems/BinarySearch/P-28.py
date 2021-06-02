# 고정점 찾기

def binary_search(array,n,start,end) :
    while start <= end:
        mid = (start+end) // 2
        if(mid == array[mid]) :
            return mid
        elif array[mid] > n :
            end = mid - 1
        else :
            start = mid + 1
    return None

n = int(input())
board = list(map(int,input().split()))

result = binary_search(board,n,0,n)

if result == None :
    print("-1")
else:
    
    print(result)