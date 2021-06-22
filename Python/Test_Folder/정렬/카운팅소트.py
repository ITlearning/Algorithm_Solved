# 일반적으로 가장 큰 데이타와 가장 작은 데이터의 차이가 백만을 넘지 않을때 효과적이다.
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i,end=' ') # 띄어쓰기를 구분으로 등정한 횟수만큼 인덱스 출력

# 시간 복잡도 O(N+K)