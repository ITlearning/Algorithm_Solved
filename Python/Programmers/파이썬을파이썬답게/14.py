# for 문과 if 문을 한번에

# 정수를 담은 리스트 mylist를 입력받아, 이 리스트의 원소 중 짝수만 값을 제곱해 담은 새 리스트를 리턴하는 solution함수를 완성해주세요.
mylist = [3,2,6,7]
def solution(mylist) :
    answer = [number**2 for number in mylist if number % 2 == 0] # list comprehension

    return answer

t = solution(mylist)

print(t)