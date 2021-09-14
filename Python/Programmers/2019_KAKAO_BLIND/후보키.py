from itertools import combinations
def solution(relation):
    answer = []
    board = []
    index = []
    other_index = []
    combi = []

    # board 리스트에 [[학번], [이름], [전공], [학년]] 식으로 나눔
    for i in range(len(relation[0])):
        tmp = []
        for j in range(len(relation)):
            tmp.append(relation[j][i])
        board.append(tmp)
    
    # 유일성
    # 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
    for i in range(len(board)):
        #print(len(set(board[i])))
        if len(set(board[i])) == len(board[i]):
            index.append(i)
        else:
            other_index.append(i)

    # 하나로 유일성이 보장되는 것은 일단 제거
    #for i in index:
    #    del board[i]

    #for i in board:
        #print(i)

    
    # 최소성
    # 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 
    # 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.    
    for i in range(2, len(board)):
        coord = list(combinations(other_index,i))
        #print(set(coord))
        combi.append(coord)
            
    


    return 0

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))