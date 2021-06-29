def solution(A, B):
    tmp = B
    tmpA = A
    tmpB = sorted(tmp, reverse=True)
    tmpA = sorted(tmpA, reverse=True)
    cnt = 0
    for _ in range(len(A)):
        mA = tmpA[0]
        mB = tmpB[0]
        if mB > mA:
            cnt += 1
            tmpB.pop(0)
        tmpA.pop(0)
        
    print(cnt)
    return cnt