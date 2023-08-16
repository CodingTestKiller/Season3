def solution(targets):
    targets.sort(key = lambda x : [x[1],x[0]])
    answer = 0
    idx = 0
    for target in targets:
        if target[0] >= idx:
            answer += 1
            idx = target[1]
    return answer