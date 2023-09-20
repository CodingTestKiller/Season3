def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5

    for i in range(len(cities)):
        if cities[i].upper() in cache:
            cache.remove(cities[i].upper())
            cache.append(cities[i].upper())
            answer += 1
        else:
            if cacheSize == len(cache):
                cache.remove(cache[0])
            cache.append(cities[i].upper())
            answer += 5
    return answer
