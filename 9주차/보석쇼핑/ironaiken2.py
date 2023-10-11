def solution(gems):
    types = set(gems)
    if len(types) == 1:
        return [1, 1]
    dic = {}
    
    for t in types:
        dic[t] = 0    
        
    s, e = 0, 0
    cnt = 0
    ans = []
    while e < len(gems) and s < len(gems):
        if cnt < len(types):
            if dic[gems[e]] == 0:
                cnt += 1
            dic[gems[e]] += 1
            if cnt < len(types):
                e += 1
        else:
            dic[gems[s]] -= 1
            if dic[gems[s]] == 0:
                cnt -= 1
                ans.append((s, e, e-s+1))
                e += 1
            s += 1
    
    ans.sort(key = lambda x:[x[2]])
    
    return [ans[0][0]+1, ans[0][1]+1]