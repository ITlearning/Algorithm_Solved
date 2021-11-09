# 로마 숫자

loma = {"I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000, "IV": 4, 
        "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

number = { 1: "I", 5: "V", 10: "X", 50: "L",
        100: "C", 500: "D", 1000: "M", 4: "IV", 
        9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

control = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9,5,4, 1]

num = []

one_loma = list(input().rstrip())
two_loma = list(input().rstrip())
one_index = 0
two_index = 0

# 입력받은 첫 번째 로마숫자 -> 아라비아숫자
while one_index < len(one_loma):
    tmp = one_loma[one_index:one_index+2]
    trans = "".join(tmp)
    # 예외상황인 작은숫자가 앞에 있는 상황인지 아닌지 체크
    if trans in loma:
        num.append(loma[trans])
        one_index += 2
    else:
        num.append(loma[one_loma[one_index]])
        one_index += 1

# 입력받은 두 번째 로마숫자 -> 아라비아숫자
while two_index < len(two_loma):
    tmp = two_loma[two_index:two_index+2]
    trans = "".join(tmp)
    if trans in loma:
        num.append(loma[trans])
        two_index += 2
    else:
        num.append(loma[two_loma[two_index]])
        two_index += 1

answer = "" # 더한 숫자를 로마숫자로 바꾼 것을 저장할 String
total_num = sum(num) # 모든 수의 합
control_index = 0 # 인덱싱할 숫자

# while문을 돌면서 숫자가 0이 될때까지 돌림
while total_num != 0:
    # 돌리는데, 가장 큰 수부터 빼면서 해당되는 문자 추가
    if total_num >= control[control_index]:
        answer += number[control[control_index]]
        total_num -= control[control_index]
    else:
        control_index += 1

print(sum(num))
print(answer)