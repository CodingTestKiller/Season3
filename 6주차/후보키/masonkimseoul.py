from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    cols = []
    for i in range(1, col + 1):
        cols.extend(combinations(range(col), i))

    is_unique = []
    for c in cols:
        tmp = [tuple(item[i] for i in c) for item in relation]

        if len(set(tmp)) == row:
            is_unique.append(c)

    is_minimum = set(is_unique)
    for i in range(len(is_unique)):
        for j in range(i + 1, len(is_unique)):
            if len(is_unique[i]) == len(set(is_unique[i]) and set(is_unique[j])):
                is_minimum.discard(is_unique[j])

    return len(is_minimum)