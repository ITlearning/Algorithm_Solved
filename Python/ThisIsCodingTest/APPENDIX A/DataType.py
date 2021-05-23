# 자료형 예시 코드들


# 리스트 컴프리헨션(List Comprension)
# 리스트를 초기화 하는 방법 중 하나

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print (array)

# N x M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(10)]
print(array)
# 언더바는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 사용한다.
# 특정한 크기를 가지는 2차원 리스트를 초기화 할 때에는 리스트 컴프리헨션을 이용해야 한다는 점을 기억하자.

# 파이썬의 특정 값 제거 방법 (여러개 제거하고 싶을 때)

a = [1,2,3,4,5,5]
remove_set = {3,5}

# remove_set에 포함되지 않는 값만 저장
array = [i for i in a if i not in remove_set]
print(array)

# 사전 자료형
# 공간 활용성이 좋다. 필요할때만 추가하고 삭제하고 하면 되는 거니까
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

if '사과' in data :
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 사전 자료형 관련 함수

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list :
    print(data[key])


# 집합 자료형
# 집합 자료형은 중복을 허용하지 않는다. 또한 순서가 없어 인덱스적 접근이 불가능하다.
# 집합 자료형 초기화 방법 1
data = set([1,1,2,3,4,4,5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1,1,2,3,4,4,5}
print(data)

# 집합 자료형 연산
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print("집합 자료형 연산")
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 집합 자료형 관련 함수
data = set([1,2,3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)