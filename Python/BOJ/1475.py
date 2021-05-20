num = input()
number = [0] * 10

sixNine = 0

for i in range(10):
    number[i] = num.count(str(i))
    if i == 6 or i == 9 :
        number[i] = 0
        sixNine += num.count(str(i))

big = max(number)

if sixNine%2 == 0 :
    sixNine//=2
else :
    sixNine = sixNine//2+1

answer = max(sixNine,big)

print(answer)
