# 반복수열
import sys
input = sys.stdin.readline

a,p = map(int, input().split())

# 처음 입력 받은 수 먼저 리스트에 추가
D = [a]

# 입력받은 수를 문자열로 변환
tmp = str(a)
# 반복수열이 나올때 까지 while 문 돌리기
while D.count(int(tmp)) < 2:
    total = 0 # 합한 값을 저장할 임시 변수
    # 제곱을 해서 나오는 최대 자릿수가 6자리라는걸 알아내어, for문을 돌릴경우 n^2의 시간복잡도가 나오기에
    # 이렇게 각 케이스 별로 계산하도록 수행
    if len(tmp) == 1:
        total += pow(int(tmp), p)
    elif len(tmp) == 2:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p)
    elif len(tmp) == 3:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p) + pow(int(tmp[2]), p)
    elif len(tmp) == 4:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p) + pow(int(tmp[2]), p) + pow(int(tmp[3]), p)
    elif len(tmp) == 5:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p) + pow(int(tmp[2]), p) + pow(int(tmp[3]), p) + pow(int(tmp[4]), p)
    elif len(tmp) == 6:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p) + pow(int(tmp[2]), p) + pow(int(tmp[3]), p) + pow(int(tmp[4]), p) + pow(int(tmp[5]), p)
    # 곱하고 더해준 수를 다시 비교할 수에 저장
    tmp = str(total)
    # 리스트에 추가
    D.append(total)
# 그리고 난 뒤에 출력은 반복수열이 일어나는 지점의 인덱스를 출력
print(D.index(int(tmp)))