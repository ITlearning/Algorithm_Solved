import heapq

def solution(scoville, K):
    answer = 0
    q = []
    cnt = 0
    for i in scoville:
        heapq.heappush(q, i)
    
    
    while True:
        one = heapq.heappop(q)
        if one >= K: # 애초에 다 높은 경우
            break
        
        if not q: # 최소개수 2개가 충족되지 않을경우
            return -1
        
        two = heapq.heappop(q)
        
        if one >= K and two >= K: # 힙에서 제일 작은 두 수가 K를 넘었을 경우
            break
        # 그게 아니라면 원래 공식대로 합하여 힙에 추가
        # 하면서 카운트 증가
        tmp = one + (two*2)
        heapq.heappush(q,tmp)
        cnt += 1
        
    answer = cnt
    return answer