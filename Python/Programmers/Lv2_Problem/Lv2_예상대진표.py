def solution(n,a,b):
    answer = 1
    
    while True:
        if (a % 2 == 0 and a - 1 == b) or (a % 2 != 0 and a + 1 == b):
            return answer
        
        a = su(a)
        b = su(b)
        
        answer += 1

    return answer

def su(x):
    if x % 2 == 0:
        return int(x / 2)
    else:
        return int((x/2)+1)