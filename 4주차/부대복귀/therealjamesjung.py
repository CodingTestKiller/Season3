
n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5

from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    graph = {}
    
    for a, b in roads:
        try:
            graph[a].append(b)
        except KeyError:
            graph[a] = [b]
        try:
            graph[b].append(a)
        except KeyError:
            graph[b] = [a]

    queue = deque([destination])

    distance = [-1] * (n+1)
    distance[destination] = 0

    while queue:
        next = queue.popleft()
        for node in graph[next]:
            if distance[node] == -1:
                distance[node] = distance[next] + 1
                queue.append(node)

    for s in sources:
        answer.append(distance[s])

    return answer

print(solution(n, roads, sources, destination))