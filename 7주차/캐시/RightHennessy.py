from collections import deque

def solution(cacheSize, cities):
    
    answer = 0
    stack = deque([])
    
    for city in cities:
        city_name = city.lower()
        if city_name in stack:
            answer += 1
            stack.remove(city_name)
            stack.append(city_name)
        else:
            answer += 5
            if (cacheSize == 0):
                continue
            
            if (len(stack) >= cacheSize):
                stack.popleft()
            stack.append(city_name)
            
    return answer