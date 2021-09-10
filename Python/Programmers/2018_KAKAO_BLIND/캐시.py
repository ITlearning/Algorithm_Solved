def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize < 1:
        answer = len(cities) * 5
    else:
        for city in cities:
            #print(str(city).lower())
            # Miss
            data = str(city).lower()
            if data not in cache:
                answer += 5
                if len(cache) < cacheSize:
                    cache.append(data)
                else:
                    cache.pop(0)
                    cache.append(data)
            else:
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