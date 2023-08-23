def solution(info, edges):
    visited = [False] * len(info)
    visited[0] = True
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            is_wolf = info[child]
            if visited[parent] and not visited[child]:
                visited[child] = True
                if is_wolf:
                    dfs(sheep, wolf + 1)
                else:
                    dfs(sheep + 1, wolf)
                visited[child] = False

    dfs(1, 0)
    return max(answer)