str = input()

result = [0] * 26

for i in str :
    result[ord(i) - 97] = str.count(i) # 해당 문자가 문장에서 얼마나 사용되었는지 카운트 하는 함수

for i in result :
    print(i, end = ' ')
