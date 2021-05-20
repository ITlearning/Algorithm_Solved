a = int(input())
b = int(input())
c = int(input())

total = a * b * c
result = [0] * 10
sTotal = str(total)

for i in sTotal :
    result[ord(i) - 48] = sTotal.count(i)

for i in result :
    print(i , end = ' ')