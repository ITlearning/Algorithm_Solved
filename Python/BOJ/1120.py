# 문자열

# 계속 틀린거
"""
import sys
input = sys.stdin.readline
# sys 를 사용하면 뒤에 \n 이 들어가서 아마도 문제가 되는듯 하다.
"""

# 정답
a,b = input().split()

total = 1e9
# 문자열 b와 a의 차이를 구해서
cur = len(b)-len(a)
# 그 차이만큼 돌린다.
for i in range(cur+1):
    cnt = 0
    # 단, 돌리는것이 b는 가만히 있고, a를 움직이는 방식이다.
    # ex) A: aba__, A: _aba_, A: __aba
    #     B: abbca, B: abbca, B: abbca
    # 이렇게 돌리면서 차이가 제일 최소인 값을 구한다.
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt += 1
    total = min(total, cnt)

# 그에 대한 답!
print(total)
