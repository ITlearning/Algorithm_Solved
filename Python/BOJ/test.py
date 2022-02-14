# input() 함수를 이용하여 정수 2개를 입력
# 입력한 값을 num1, num2변수에 저장
print("첫번째 정수 입력: ", end="")
num1 = input()

print("두번째 정수 입력: ", end="")
num2 = input()

# 정수형으로 변환, num3,4 저장
 
num3 = int(num1)
num4 = int(num2)

# num1 + num2의 값 계산 후 sum1 변수 저장
sum1 = int(num1)+int(num2)

# 수식과 sum1의 값과 자료형 출력
# 수식이 뭐임 ㅇㅅㅇ;
print(num1, "+", num2, "=", sum1)
print(type(sum1))
print()

# num3 + num4 값 계산 후 sum2 변수 저장
sum2 = num3 + num4
print(num3, "+", num4, "=", sum2)
print(type(sum2))

