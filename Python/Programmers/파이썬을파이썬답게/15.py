# flag OR else
# 본 문제에서는 자연수 5개가 주어집니다.
# 숫자를 차례로 곱해 나온수가 제곱수가 되면 found를 출력하고
# 모든 수를 곱해도 제곱수가 나오지 않는다면 not found를 출력하세요

import math

numbers = [int(input()) for i in range(5)]

multiplied = 1
# for-else 문을 쓰면 flag를 사용하지 않아도 T,F 구분의 코드 작성이 가능합니다.
for number in numbers :
    multiplied *= number
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)) :
        print("found")
        break
else :
    print("not found")