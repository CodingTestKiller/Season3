from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    answer = 0

    for city in cities:
        city = city.lower()
        if city not in cache:
            cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer

