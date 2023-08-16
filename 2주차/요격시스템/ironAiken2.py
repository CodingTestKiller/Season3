def solution(targets):
    targets.sort(key=lambda x:list(reversed(x)))
    
    ans, end = 0, 0
    for target in targets:
        if end <= target[0]:
            ans += 1
            end = target[1]
    
    return ans