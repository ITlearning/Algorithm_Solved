# 함수 구현
# 부스트캠프 2019년 코딩 테스트 문제
'''
from collections import Counter
# 위 라이브러리는 리스트에 존재하는 것들에 대한 카운트를 셀 수 있는 라이브러리
arr = [3,5,7,1,1]
b = Counter(arr)
t = True


for key,val in dict(b).items():
    if val >= 2 :
        print(val, end=" ")
        t = False

if t == True:
    print(-1)
'''
answer = []
arr = [3,3,2,4,4,2,5,2,5,5]
tmp = []
for i in arr:
    if i not in tmp:
        tmp.append(i)
print(tmp)
for i in tmp:
    if arr.count(i) >= 2:
        answer.append(arr.count(i))

if len(answer) == 0:
    answer.append(-1)
    print(answer)
else:
    print(answer)

