# 20분

from itertools import combinations

def solution(relation):

    global keys
    keys = []
    table = list(map(list, zip(*relation)))
    r, c = len(table), len(table[0])

    combi = []
    for i in range(1, r+1):
        combi.extend(map(list, list(combinations(range(r), i))))

    for com in combi:
        stack = []
        for y in range(c):
            tmp = [table[x][y] for x in com]
            if tmp not in stack:
                stack.append(tmp)
        if len(stack) == c and check(com):
            keys.append(com)

    return len(keys)

def check(tmp):
    for key in keys:
        count = 0
        for k in key:
            if k in tmp:
                count += 1
        if count == len(key):
            return False
            
    return True