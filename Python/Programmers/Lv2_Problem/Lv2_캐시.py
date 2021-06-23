def solution(cacheSize, cities):
    answer = 0
    cache = []
    # LRU(Least Recently Used) 캐시 교체 알고리즘
    # 사용하는 캐시에 새로운 데이터가 발생했을 때, 가장 오래전에 사용된 데이터를
    # 제거하고 새로운 데이터를 삽입하는 알고리즘
    working_time = 0
    for city in cities:
        # 대소문자 구분없이 사용하기 위해 모든 입력 소문자
        city = city.lower()
        if city not in cache:
            # Miss = 새로운 데이터가 들어온 경우
            # 1. 캐시에 넣어준다
            # 2. 캐시가 가득 찼다면, 가장 오래된 데이터를 지우고 넣어준다.
            if len(cache) < cacheSize:
                cache.append(city)
                working_time += 5
            else:
                # 캐시 사이즈가 0일 경우도 따져야 한다.
                # 0일때는 아무짓도 하지 않고 워킹 타임만 늘린다.
                if cacheSize == 0:
                    working_time += 5
                    continue
                cache.pop(0)
                cache.append(city)
                working_time += 5
        # Hit = 존재하는 데이터가 들어온 경우
        # 1. 해당 데이터를 꺼낸 뒤에,
        # 2. 가장 최근 데이터 위치로 보내준다.
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            working_time += 1
    return working_time