from collections import deque

def solution(n):
    answer = 0
    while n > 0:
        answer += n % 2
        n //= 2
        
    return answer