# 문자열 뒤집기

# 내 풀이 ;ㅁ;
'''
s = input()

zero = s.count('0')
one = s.count('1')
count = 0
result = 0
t = True
if zero >= one :
    while count <= len(s)-1:
        if s[count] == "1" :
            if t == True:
                result += 1
                t = False
                count += 1
            else :
                count += 1
        elif s[count] == "0" :
            count += 1
            t = True
else :
    while count <= len(s)-1:
        if s[count] == "0" :
            if t == True:
                result += 1
                t = False
                count += 1
            else :
                count += 1
        elif s[count] == "1" :
            count += 1
            t = True


print(result)
'''
# 해답
s = input()
count = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1

print((count+1) // 2)

# 머리가 안좋으면 고생한다...