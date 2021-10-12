# 도서관
n,m = map(int,input().split())

board = list(map(int,input().split()))
minus = []
plus = []
index = 0

# 0을 기준으로 음수 양수 나눔
for i in board:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

# 절댓값기준으로 가장 큰 수 저장
big_number = 0
for i in board:
    if abs(i) > abs(big_number):
        big_number = i

# 양수는 반대로 정렬
# 음수는 정방향으로 정렬
plus.sort(reverse=True)
minus.sort()
total = []

# 먼저 음수를 입력 받은 m의 위치에 해당하는 숫자들 뽑아주기
for i in range(0, len(minus), m):
    # 근데? 아까 저장해논 큰 수랑 같으면 넣지 않음
    if minus[i] != big_number:
        total.append(minus[i])

# 양수도 똑같이
for j in range(0, len(plus), m):
    if plus[j] != big_number:
        total.append(plus[j])

# 답에 먼저 저장해놓은 수 절대값으로 입력
answer = abs(big_number)
# 그리고 뽑아온 숫자들 *2 해서 넣어줌
for num in total:
    answer += abs(num*2)

# 답 출력
print(answer)
