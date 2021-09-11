def reload(num,b,sx,sy,ex,ey, point):
    if num == 1:
        tmp = sy
        while sx < ex+1:
            if sy > ey:
                sx += 1
                sy = tmp
                continue
            b[sx][sy] -= point
            sy += 1

        '''
        for i in range(sx, ex+1):
            for j in range(sy,ey+1):
                b[i][j] -= point
        '''
    elif num == 2:
        tmp = sy
        while sx < ex+1:
            if sy > ey:
                sx += 1
                sy = tmp
                continue
            b[sx][sy] += point
            sy += 1
        '''
        for i in range(sx, ex+1):
            for j in range(sy,ey+1):
                b[i][j] += point
        '''

def binary_search(answer, target, start, end):
    total = 0
    while start < end:
        mid = (start+end) // 2
        if answer[mid] < target:
            total = mid
            start = mid + 1
        elif answer[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return total

def solution(board, skill):
    answer = 0

    for i in skill:
        # 적 입력 시
        if i[0] == 1:
            start_x, start_y = i[1],i[2]
            end_x, end_y = i[3],i[4]
            attack = i[5]
            reload(i[0],board,start_x,start_y,end_x,end_y, attack)
        # 아군 입력 시
        elif i[0] == 2:
            start_x, start_y = i[1],i[2]
            end_x, end_y = i[3],i[4]
            heal = i[5]
            reload(i[0],board,start_x,start_y,end_x,end_y, heal)


    an = sum(board,[])
    an.sort()
    #print(an)
    total = len(an)
    total -= binary_search(an,1,0,len(an)-1) + 1

    return total

print(solution(	[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))