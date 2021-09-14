from itertools import combinations
def solution(relation):
    board_list = []

    row = len(relation)
    col = len(relation[0])

    # 모든 조합 구하기
    for i in range(1, col+1):
        board_list.extend(combinations(range(col),i))
    print(board_list)
    
    # 유일성 구하기
    unique = []
    for board in board_list:
        tmp = [tuple([item[i] for i in board]) for item in relation]
        print(set(tmp))
        if len(set(tmp)) == row:
            unique.append(board)
    
    # 최소성 구하기
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    print(answer)
    #print(tmp)
            



    return len(answer)

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))