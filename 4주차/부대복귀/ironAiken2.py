from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    dist = [-1] * (n+1)
    dist[destination] = 0
    queue = deque([destination])
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if dist[node] == -1:
                dist[node] = dist[now] + 1
                queue.append(node)
    
    ans = []
    for s in sources:
        ans.append(dist[s])
        
    return ans
    

