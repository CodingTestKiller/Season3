import sys
sys.setrecursionlimit(10**6)
cnt = 0
def post_order(a,tree,pos):
    global cnt
    if tree[pos][1]:
        post_order(a,tree,tree[pos][1])
    if tree[pos][2]:
        post_order(a,tree,tree[pos][2])
    if a[pos] == 0:
        return
    if pos == 0:
        return
    a[tree[pos][0]] += a[pos]
    cnt += abs(a[pos])
    a[pos] = 0
    
def solution(a, edges):
    from collections import deque
    n = len(a)
    tree = [[0,0,0] for _ in range(n)]
    graph = [[] for _ in range(n)]
    q = deque()
    for edge in edges:
        cur = edge[0]
        nxt = edge[1]
        graph[cur].append(nxt)
        graph[nxt].append(cur)
    tree[0][0] = -1
    visit = [False] * (n)
    q.append(0)
    visit[0] = True
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visit[nxt]:
                if not tree[cur][1]:
                    tree[cur][1] = nxt
                else:
                    tree[cur][2] = nxt
                tree[nxt][0] = cur
                q.append(nxt)
                visit[nxt] = True
    post_order(a,tree,0)
    if a[0] == 0:
        answer = cnt
    else:
        answer = -1
    print(a)
    print(cnt)
    return answer