# 접두사 찾기
# 문자열 S의 접두사란 S의 가장 앞에서부터 부분 문자열을 의미한다. 
# 예를 들어, S = "codeplus"의 접두사는 "code", "co", "codepl", "codeplus"가 있고, "plus", "s", "cude", "crud"는 접두사가 아니다.
# 총 N개의 문자열로 이루어진 집합 S가 주어진다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 문자열 중 적어도 하나의 접두사인 것의 개수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

# 1. 문자열 저장
strings = [input().strip() for _ in range(n)]

cnt = 0
# 2. 문자열 외에 문자들 입력받기
for _ in range(m):
    pattern = input().rstrip()
    # 3. 입력받은 문자를 문자열과 비교하면서 접두사면 카운트
    for s in strings:
        if s.startswith(pattern):
            cnt += 1
            break

print(cnt)
