from collections import deque

def solution(a, edges):
    
    visited = [False]*len(a)
    edge_info = [[] for _ in range(len(a))]
    list_a = a
    stack = []
    parent = [0]*len(a)

    for edge in edges:
        edge_info[edge[0]].append(edge[1])
        edge_info[edge[1]].append(edge[0])

    queue = deque([0])
    while queue:
        n = queue.popleft()
        if not visited[n]:
            stack.append(n)
            visited[n] = True
            for x in edge_info[n]:
                if visited[x]:
                    parent[n] = x
                else:
                    queue.append(x)

    count = 0
    while len(stack) > 1:
        n = stack.pop()
        list_a[parent[n]] += list_a[n]
        count += abs(list_a[n])

    if len(stack) == 0:
        return -1
    
    n = stack.pop()
    if list_a[n] == 0:
        return count
    else:
        return -1

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
