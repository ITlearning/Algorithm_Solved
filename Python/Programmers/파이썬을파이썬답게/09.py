# map 함수 이용하기

# 정수를 담은 이차원 리스트, mylist가 solution 함수의 파라미터로 주어집니다.
# solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성하라.
mylist = [[1],[2]]
def solution(mylist) :
    answer = list(map(len, mylist))
    return answer

t = solution(mylist)
print(t)
