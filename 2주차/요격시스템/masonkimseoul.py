def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1])
    pos = 0
    for i in targets:
        if pos <= i[0]:
            answer += 1
            pos = i[1]
    return answer