from collections import deque

def solution(n, roads, sources, destination):

    que_bfs = deque([destination])

    global distance_list
    distance_list = [-1 for _ in range(n+1)]

    global roads_list
    roads_list = [[] for _ in range(n+1)]
    for road in roads:
        roads_list[road[0]].append(road[1])
        roads_list[road[1]].append(road[0])

    distance_list[destination] = 0
    while que_bfs:
        item = que_bfs.popleft()
        for child in roads_list[item]:
            if distance_list[child] == -1:
                que_bfs.append(child)
                distance_list[child] = distance_list[item]+1

    answer = []
    for source in sources:
        answer.append(distance_list[source])
    return answer