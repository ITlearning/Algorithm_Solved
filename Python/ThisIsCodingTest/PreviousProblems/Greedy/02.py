# 곱하기 혹은 더하기

s = input()
result = int(s[0])
for i in s[1:] :
    num = int(i)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)