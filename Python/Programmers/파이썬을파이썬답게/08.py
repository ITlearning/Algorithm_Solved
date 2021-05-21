# 모든 멤버의 type변환하기

# 문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수, solution 

def solution(mylist):
    answer = []
    answer = list(map(int, mylist))
    return answer