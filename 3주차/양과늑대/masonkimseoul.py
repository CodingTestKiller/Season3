def solution(info, edges):
    answer = []
    visited = [False] * len(info)

    def DFS(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for p1, p2 in edges:
            if not visited[p2] and visited[p1]:
                visited[p2] = True
                if info[p2] == 0:
                    DFS(sheep + 1, wolf)
                else:
                    DFS(sheep, wolf + 1)
                visited[p2] = False

    visited[0] = True
    DFS(1, 0)
    return max(answer)