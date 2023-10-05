import heapq

def solution(n, paths, gates, summits):
    answer = [-1, 10000001]
    graph = [[] for _ in range(n + 1)]
    distance = [10000001] * (n + 1)
    is_summit = [False] * (n + 1)

    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    for i in summits:
        is_summit[i] = True
    summits.sort()

    queue = []
    for i in gates:
        distance[i] = 0
        heapq.heappush(queue, [i, 0])
    while queue:
        gate, dist_tmp = heapq.heappop(queue)

        if is_summit[gate] or distance[gate] < dist_tmp:
            continue

        for node, dist_tmp in graph[gate]:
            dist_tmp = max(distance[gate], dist_tmp)
            if distance[node] > dist_tmp:
                distance[node] = dist_tmp
                heapq.heappush(queue, [node, dist_tmp])

    for i in summits:
        if distance[i] < answer[1]:
            answer[0] = i
            answer[1] = distance[i]

    return answer