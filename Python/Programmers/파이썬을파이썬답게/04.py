# 문자열 정렬하기
# 문자열 s와 자연수 n이 입력으로 주어집니다. 문자열 s를 좌측/ 가운데/ 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트 해보세요.

s, n = input().strip().split(' ')
n = int(n)


print(s.ljust(n))   # 좌측 정렬
print(s.center(n))  # 중앙 정렬
print(s.rjust(n))   # 우측 정렬