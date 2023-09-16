#2시 40분 시작
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city_none in cities:
        city = city_none.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.append(city)
                cache.popleft()

                
    return answer