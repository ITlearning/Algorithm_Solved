from itertools import combinations
from collections import Counter
def solution(clothes):
    answer = 0
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