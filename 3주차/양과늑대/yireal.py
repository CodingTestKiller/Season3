def solution(info, edges):
    visit = [False] * len(info)
    answer = []
    def dfs(sheep,wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for cur,nxt in edges:
            if visit[cur] and not visit[nxt]:
                visit[nxt] = True
                if info[nxt] == 0:
                    dfs(sheep + 1 ,wolf)
                else:
                    dfs(sheep,wolf + 1)
                visit[nxt] = False
    visit[0] = True
    dfs(1,0)
    return max(answer)