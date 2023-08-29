from collections import defaultdict
from collections import deque


def BFS(n, graph, start):
    distance_list = [-1 for _ in range(n+1)]
    q = deque()
    q.append((start, 0))
    while q:
        now_pos, now_depth = q.popleft()
        if distance_list[now_pos] == -1:
            distance_list[now_pos] = now_depth
        else:
            continue
        for new_pos in graph[now_pos]:
            q.append((new_pos, now_depth+1))
    return distance_list


def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)

    for v1, v2 in roads:
        graph[v1].append(v2)
        graph[v2].append(v1)

    dest = BFS(n, graph, destination)

    for i in sources:
        answer.append(dest[i])

    return answer
