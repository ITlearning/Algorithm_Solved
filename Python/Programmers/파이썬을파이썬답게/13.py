# 가장 많이 등장하는 알파벳 찾기
# 이 문제에는 표준입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성하라.

import collections

mystr = input().strip()
                                    # most_common() 함수가 개수가 가장 많은 순으로 정렬해주는 함수이다.
counter = collections.Counter(mystr).most_common() # 데이터의 개수가 가장 많은 순 정렬 

maxValue = max(collections.Counter(mystr))

total = ""

for i in range(len(counter)) :
    if counter[i][1] == counter[0][1] :
        total += counter[i][0]

print(''.join(sorted(list(total))))