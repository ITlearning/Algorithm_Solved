from itertools import combinations
def solution(relation):
    #turn = list(zip(*relation[::1]))
    #for i in turn:
        #print(i)
    total = set()
    cnt = 0
    t = []
    line = [1,2,3,4]
    if len(relation) != 0:
        col = len(relation[0])
        row = len(relation)

    for i in range(1,col+1):
            # extend
            t.extend([set(k) for k in combinations([j for j in range(col)],i)])
    print(t)
    #print(cnt) 
    return 0

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))