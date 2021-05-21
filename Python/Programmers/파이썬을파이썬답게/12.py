# 순열과 조합
# 숫자를 담은 일차원 리스트,mylist 에 대해 mylist 원소로 이루어진 모든 순열을 사전순으로 리턴하는 solution을 완성해주세요.

from itertools import permutations

mylist = [2,1]

def solution(mylist) :
    answer = []
    mylist = sorted(mylist)
    answer = list(map(list,permutations(mylist)))
    return answer

t = solution(mylist)

print(t)

# 일차원 리스트가 먼저 오름차순으로 정렬이 되어있으면 다행인데, 위 코드처럼 뒤죽박죽으로 되어있을 때가 있을 경우를 생각해서
# sorted() 함수를 사용하여 일단 크기순으로 정렬하고 순열의 조합을 짜게 했다.