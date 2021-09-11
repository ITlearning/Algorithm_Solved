from itertools import combinations
def solution(n, info):
    answer = []
    
    info.reverse()
    apeach = 0
    ryan = 0
    com = [0,1,2,3,4,5,0,0,0,0]
    a = list(combinations(com, 5))
    print(a)
    # 어피치 총 점수 알아내기
    for idx, val in enumerate(info):
        apeach += idx * val


    print(apeach)

    return answer

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
