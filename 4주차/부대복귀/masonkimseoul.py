from collections import deque

def solution(n, roads, sources, destination):
    visited = [-1] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)

    queue = deque([destination])
    visited[destination] = 0

    while queue:
        pos = queue.popleft()
        for i in graph[pos]:
            if visited[i] == -1:
                visited[i] = visited[pos] + 1
                queue.append(i)

    return [visited[i] for i in sources]