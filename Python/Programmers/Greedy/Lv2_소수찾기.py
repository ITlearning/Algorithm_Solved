import math
from itertools import permutations

def prime_number(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

def solution(numbers):
    answer = []
    
    for i in range(1,len(numbers)+1):
        arr = list(permutations(numbers,i))
        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))
            if prime_number(num):
                answer.append(num)
                
    answer = list(set(answer))
    return len(answer)