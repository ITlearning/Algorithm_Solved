# 2차원 리스트 뒤집기
# solution 함수는 이차원 리스트, mylist를 인자로 받습니다
# solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야 합니다. 

# 예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우,
# solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

def solution(mylist):
    answer = list(map(list,zip(*mylist))) #zip 함수를 이용하면 각 리스트에 하나씩을 뽑아온다
    return answer