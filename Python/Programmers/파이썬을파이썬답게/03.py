# n진법으로 표기된 string을 10진법 숫자로 변환하기
# base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.

# 복잡하게 생각하지말고 기존에 주어진 함수를 사용하자.

num, base = map(int, input().strip().split(' '))
num = str(num)
answer = int(num,base)

print(answer)