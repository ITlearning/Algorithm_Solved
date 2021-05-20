# 우선 다 입력받고 sorted 돌려서 오름차순 정렬 후 더해서 비교

n = int(input())

number = input().split()
for i in range(len(number)) :
    number[i] = int(number[i])

number = sorted(number)
total = int(input())
start = 0
end = len(number) - 1

cnt = 0
while start < end :
    if number[start] + number[end] == total :
        cnt += 1
        start += 1
        end -= 1
    elif number[start] + number[end] < total :
        start += 1
    elif number[start] + number[end] > total :
        end -= 1

print(cnt)
