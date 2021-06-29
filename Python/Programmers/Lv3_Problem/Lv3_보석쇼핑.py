def solution(gems):
    answer = []
    gem_len = len(gems) + 1
    overlap = len(set(gems))
    start = 0
    end = 0
    dic = {}
    
    while end < len(gems):
        
        if gems[end] not in dic:
            dic[gems[end]] = 1  # 추가
        else:
            dic[gems[end]] += 1 # 이미 있으면 수 증가
            
        end += 1
        
        if len(dic) == overlap:
            while start < end:
                if dic[gems[start]] > 1:
                    dic[gems[start]] -= 1
                    start += 1
                
                elif gem_len > end - start:
                    gem_len = end - start
                    answer = [start+1, end]
                    break
                
                else:
                    break
    
    return answer