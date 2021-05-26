# 문자열 재정렬

# 문자열과 수 입력
s = input()
# 문자열을 따로 저장할 공간
copy = ""
# 먼저 sorting을 해줌, 이러면 숫자가 제일 앞에,정렬된 문자들이 뒤에 나온다.
s = sorted(s)
num = 0
for i in s:
    # 숫자일 경우에 if문 들어가고 아닐 경우엔 else문 진입
    if int(ord(i)) < 65 : 
        num += int(ord(i)) - int(ord('0'))
    else :
        copy = copy + i

# for 문을 다 돌고 더해진 숫자들 기입
# 숫자가 0이 아닐경우에만 동작
if num != 0:
    copy += str(num)

print(copy)