# 2차원 리스트 값 업데이트 함수
def reload(num,b,sx,sy,ex,ey, point):
    # 적 공격시 값 빼기
    if num == 1: 
        for i in range(sx, ex+1):
            for j in range(sy,ey+1):
                b[i][j] -= point
                
    # 아군 힐러 시 값 더하기
    elif num == 2:
        for i in range(sx, ex+1):
            for j in range(sy,ey+1):
                b[i][j] += point

def solution(board, skill):
    
    # 입력받은 스킬 돌리면서
    for i in skill:
        # 적 입력 시
        if i[0] == 1:
            # 해당하는 값 추출
            start_x, start_y = i[1],i[2]
            end_x, end_y = i[3],i[4]
            attack = i[5]
            # reload() 함수 돌리기
            reload(i[0],board,start_x,start_y,end_x,end_y, attack)
        # 아군 입력 시
        elif i[0] == 2:
            # 해당하는 값 추출
            start_x, start_y = i[1],i[2]
            end_x, end_y = i[3],i[4]
            heal = i[5]
            # reload() 함수 돌리기
            reload(i[0],board,start_x,start_y,end_x,end_y, heal)


    total = 0
    # 0보다 작은 수의 개수 빼고 카운트
    for i in board:
        for j in i:
            if j > 0:
                total += 1

    return total