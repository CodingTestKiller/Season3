import heapq
from math import inf

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True

    distance = [inf] * (n + 1)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue, [0, gate])

    while queue:
        d, i = heapq.heappop(queue)
        if distance[i] < d or is_summit[i]:
            continue
        for j, dd in graph[i]:
            dd = max(distance[i], dd)
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(queue, [dd, j])

    result = [-1, inf]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
            
    return result