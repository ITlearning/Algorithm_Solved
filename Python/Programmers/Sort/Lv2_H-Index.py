def solution(citations):
    citations.sort(reverse=True)
    cnt = 0
    for i in range(1,len(citations)+1):
        if citations[i-1] >= i:
            cnt += 1
    return cnt