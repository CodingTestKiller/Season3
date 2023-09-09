def solution(cards):
    is_visited = [0 for _ in range(len(cards))]
    box = [[] for _ in range(len(cards))]
    cnt, flag = 0, 0
    for i in range(len(cards)):
        flag = 0
        while is_visited[i] != 1:
            box[cnt].append(cards[i])
            is_visited[i] = 1
            i = cards[i] - 1
            flag += 1
        if flag != 0:
            cnt += 1

    answer = list()
    for i in range(cnt):
        answer.append([box[i], len(box[i])])

    answer.sort(key = lambda x: -x[1])
    if len(answer) > 1:
        return answer[0][1] * answer[1][1]
    else:
        return 0