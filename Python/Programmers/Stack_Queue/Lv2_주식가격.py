from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    t = len(prices)
    while t != 0:
        cnt = 0
        tmp = prices.popleft()
        for i in prices:
            cnt += 1
            if tmp > i :
                break
        answer.append(cnt)
        t -= 1
    
    return answer