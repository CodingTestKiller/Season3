import sys
sys.setrecursionlimit(10**6)


def is_possible(visited, tree, now):
    global ans
    visited[now] = True
    child = tree[now][0]
    val = tree[now][1]

    for c in child:
        if visited[c] == False:
            v = is_possible(visited, tree, c)
            ans += abs(v)
            val += v

    return val


def solution(a, edges):
    if sum(a) != 0:
        return -1

    global ans
    ans = 0
    tree = [[[]] for _ in range(len(a))]
    visited = [False for _ in range(len(a))]

    for edge in edges:
        tree[edge[0]][0].append(edge[1])
        tree[edge[1]][0].append(edge[0])
    for i, value in enumerate(a):
        tree[i].append(value)

    if is_possible(visited, tree, 0) == 0:
        return ans
