# 주요 라이브러리

''' 내장 함수 '''

# sum 함수
result = sum([1,2,3,4,5]) # 모든 원소의 합을 반환한다.
print(result)

# min ,max함수
result = min([1,2,3,4,5]) # 파라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환한다.
print(result)

result = max(1,2,3,4)
print(result)

# eval 함수
result = eval("(3+5)*7") # 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
print(result)

''' itertools 라이브러리 '''

from itertools import permutations

# 순열 구하기
data = ['A','B','C']
result = list(permutations(data,3)) # 모든 순열 구하기, 뒤에 숫자를 변경하면 그 수 만큼의 조합을 구해준다.
print(result)

from itertools import product
# 조합 구하기
result = list(product(data,repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)


''' heapq 라이브러리 '''

# heapq로 힙 정렬(Heap Sort)을 구현하는 예제
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

''' 파이썬은 기본적으로 최소힙을 제공하고 최대힙을 제공하지 않는다. '''
''' 따라서 heapq 라이브러리를 이용하여 최대힙을 구현해야 할 때는 '''
''' 원소의 부호를 임시로 변경하는 방식을 사용해야 한다. '''

def maxheapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = maxheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)


''' bisect '''
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4
print(bisect_left(a,x)) # 리스트 a에 데이터x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
print(bisect_right(a,x)) # 오른쪽 메서드

# 값이 특정 범위에 속하는 원소의 개수 를 구하는 코드

# 값이[left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

# 리스트 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))


''' collections 라이브러리 '''
from collections import deque
data = deque([2,3,4])
data.appendleft(1) # 왼쪽 끝 추가
data.append(5)
print(data)
print(list(data)) # 리스트 자료형으로 변환

from collections import Counter
# Counter 기능
counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])

print(counter['blue'])  # blue가 등장한 횟수
print(counter['green']) # green이 등장한 횟수
print(dict(counter))    # 사전 자료형으로 변환


''' math 라이브러리 '''
import math
print(math.factorial(5)) # 5팩토리얼 출력
print(math.sqrt(7))      # 7의 제곱근을 출력
print(math.gcd(21,14))   # 21과 14의 최대 공약수 출력
print(math.pi)           # 파이(pi) 출력
print(math.e)            # 자연상수 e 출력