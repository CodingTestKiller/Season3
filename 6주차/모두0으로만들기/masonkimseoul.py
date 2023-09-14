import sys
sys.setrecursionlimit(10 ** 6)

def solution(a, edges):
    global answer
    answer = 0

    length = len(a)
    graph = [[] for _ in range(length)]
    is_visited = [0] * length

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    def DFS(node, a, graph):
        global answer
        pos = a[node]
        is_visited[node] = 1

        for i in graph[node]:
            if is_visited[i] == 0:
                pos += DFS(i, a, graph)

        answer += abs(pos)
        return pos

    DFS(0, a, graph)
    if sum(a) != 0:
        answer = -1
    return answer