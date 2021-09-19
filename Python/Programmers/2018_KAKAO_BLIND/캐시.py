def solution(cacheSize, cities):
    answer = 0
    cache = []

    
    # 만일 사이즈가 0일 경우
    if cacheSize < 1:
        # 모든게 다 캐시 미스이니 길이에 * 5 해준다.
        answer = len(cities) * 5   
    
    # 0 이상일 경우
    else:
        for city in cities:
            
            # Miss
            data = str(city).lower()
            # 데이터가 기존에 존재하지 않으면
            if data not in cache:
                answer += 5
                # 캐시 사이즈보다 캐시가 적을 경우엔 추가해주고
                if len(cache) < cacheSize:
                    cache.append(data)
                # 크면 제일 먼저 넣어놨던거 빼고 추가
                else:
                    cache.pop(0)
                    cache.append(data)
            
            # Hit
            else:
                # 기존에 있으면 기존에 존재하는 데이터 뽑아서 제일 뒤에 넣어줌
                answer += 1
                cache.pop(cache.index(data))
                cache.append(data)


        
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 16분 03초