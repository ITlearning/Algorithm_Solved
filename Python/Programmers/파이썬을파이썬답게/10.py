# sequence 멤버를 하나로 이어붙이기

# 문자열 리스트 mylist 를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어라.

mylist = ["1", "100", "33"]
def solution(mylist) :
    answer = ''.join(mylist)
    return answer

t = solution(mylist)

print(t)
