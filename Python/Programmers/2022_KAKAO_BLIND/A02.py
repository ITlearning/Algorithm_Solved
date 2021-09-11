import math

NOTATION = '0123456789ABCDEF'
def change(number,k):
    q,r = divmod(number,k)
    n = NOTATION[r]
    return change(q,k) + n if q else n


def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    tmp = change(n,k)

    tt = tmp.split('0')
    #print(tt)
    if '1' in tt:
        while '1' in tt:
            tt.remove('1')
    if '' in tt:
        while '' in tt:
            tt.remove('')

    for i in tt:
        if is_prime(int(i)):
            answer += 1
    #print(tt)


    return answer

print(solution(437674, 3))
print(solution(110011,10))
print(solution(2,10))