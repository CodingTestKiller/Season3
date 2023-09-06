from itertools import combinations

def solution(line):
    graph = list(combinations(line, 2))
    stars = []

    for i in graph:
        A, B, E = i[0]
        C, D, F = i[1]

        if A * D - B * C == 0:
            continue
        else:
            x = (B * F - E * D) / (A * D - B * C)
            y = (E * C - A * F) / (A * D - B * C)
            if x == int(x) and y == int(y):
                stars.append([int(x), int(y)])
    x_max = stars[0][0]
    x_min = stars[0][0]
    y_max = stars[0][1]
    y_min = stars[0][1]
    for i in stars:
        x_max = max(x_max, i[0])
        x_min = min(x_min, i[0])
        y_max = max(y_max, i[1])
        y_min = min(y_min, i[1])

    result = list()
    for i in range(y_max - y_min + 1):
        tmp = list()
        for j in range(x_max - x_min + 1):
            tmp.append('.')
        result.append(tmp)

    for i in stars:
        result[i[1] - y_min][i[0] - x_min] = '*'

    answer = list()
    for i in range(len(result) - 1, -1, -1):
        tmp = str()
        for j in result[i]:
            tmp += j
        answer.append(tmp)

    return answer