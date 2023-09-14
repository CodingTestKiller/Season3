from itertools import combinations


def solution(relation):
    columns = [list(x) for x in zip(*relation)]
    answers = []

    for i in range(1, len(columns) + 1):
        for col in combinations(range(len(columns)), i):
            flag = False
            for answer in answers:
                if set(answer).issubset(set(col)):
                    flag = True
                    break
            if flag:
                continue
            if len(set(zip(*[columns[x] for x in col]))) == len(relation):
                # print('answer', col)
                answers.append(col)
    # print(answers)
    return len(answers)