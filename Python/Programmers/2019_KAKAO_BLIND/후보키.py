from itertools import combinations
def solution(relation):
    answer = []
    board = []
    dic = {}

    # 유일성
    for i in range(len(relation)):
        t = []
        for j in range(1,len(relation[0])+1):
            tmp = list(combinations(relation[i], j))
            #print(tmp)
            tmp.sort()
            if tmp not in board:
                board.append(tmp)
    
    #print(board)
    for i in range(len(board)-1,-1,-1):
        print(set(board[i]))
        print(set(board[i-1]))
        cnt = True
        for j in range(len(board[i])-1,-1,-1):
            for k in range(len(board[i-1])):
                print(set(board[i-1][j]), set(board[i][k]))
                print(set(board[i-1][j]).issubset(set(board[i][k])))
                
                if set(board[i-1][j]).issubset(set(board[i][k])):
                    cnt = False
                    break
        
        if cnt : 
            if len(board[i]) not in answer:
                answer.append(len(board[i][0]))

            

    return answer

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))