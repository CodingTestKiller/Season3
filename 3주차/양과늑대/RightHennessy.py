# 이걸 내가 어케 품.. 
# 카카오 해설 보고도 해결 x

def solution(info, edges):
    visited = [1] + [0] * (len(info)-1)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = 0

    dfs(1, 0)

    return max(answer)