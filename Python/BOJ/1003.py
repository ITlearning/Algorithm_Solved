# 피보나치 함수

t = int(input())

for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp

    print(zero, one)

# 피보나치 수의 규칙은
# 첫째 및 둘째 항이 1 이고 그 뒤 모든 항은 바로 함 두항의 합인 수열이다.
# 따라서 0은 무조건 나오는 수이니 기본 값을 1로 잡고

# 입력된 수까지 계속 for문을 돌려서 규칙대로 점점 수를 키워나간다.

# 수가 5일 경우
# 0 = 1,0
# 1 = 0,1
# 2 = 1,1
# 3 = 1,2
# 4 = 2,3
# 5 = 3,5