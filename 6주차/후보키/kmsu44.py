import itertools


def find_candidate(key_list: list, relation: list, col: int, row: int):
    res = []
    for k in key_list:
        s = set()
        for c in range(col):
            key = ""
            for i in k:
                key += str(relation[c][i])
            s.add(key)
        if len(s) == col:
            res.append(k)
    return res


def findkey_list(num: int, num_list: list, res):
    tmp = list(itertools.combinations(num_list, num))
    L = []
    for i in tmp:
        flag = True
        k = set(i)
        for key in res:
            if key.issubset(k):
                flag = False
                break
        if flag:
            L.append(k)
    return L


def solution(relation):
    answer = 0
    res = []
    size = len(relation[0])
    col = len(relation)
    num_list = [i for i in range(size)]
    for i in range(1, size+1):
        key_list = findkey_list(i, num_list, res)
        # print(key_list)
        if key_list:
            res += find_candidate(key_list, relation, col, size)
            # print(res)

    return len(res)
