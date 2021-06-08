from itertools import combinations
from collections import Counter
def solution(clothes):
    b = []
    for i in clothes:
        b.append(i[1])
    
    countB = Counter(b)
    b = countB.values()
    valuelist = list(b)
    valuelist.sort()
    
    if len(valuelist) == 1:
        return valuelist[0]
    
    tmp = valuelist[0]
    for i in valuelist[1:]:
        tmp += i + (i*tmp)
        
    return tmp

# 공식을 알아야 한다. 공식이 항이 늘어날때마다 이전 겨로가에 더해지는 형식
'''
예) [1]
1 = 1

예) [1 2]
1 + (2 + 2 * 1) = 1 + 4 = 5

예) [1 2 3]
1 + (2 + 2 * 1) + (3 + 3 * 5) = 1 + 4 + 18 = 23
'''