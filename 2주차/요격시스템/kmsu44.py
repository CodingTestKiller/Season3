def solution(targets):
    answer = 1
    targets.sort()
    prev_s, prev_e = targets[0]
    index = 1

    while index < len(targets):
        s, e = targets[index]
        if s < prev_e:
            index += 1
            prev_e = min(prev_e, e)
        else:
            prev_s, prev_e = s, e
            index += 1

            answer += 1

    return answer
