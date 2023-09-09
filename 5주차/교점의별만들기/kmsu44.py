# 4시 44분 시작0
from itertools import combinations
import sys


def intersection_point(s1, s2):
    a, b, e = s1
    c, d, f = s2
    if a*d - b*c == 0:
        return False
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)
    if x % 1 == 0 and y % 1 == 0:
        return (int(x), int(y))
    else:
        return False


def solution(line):
    answer = []
    x_max = -sys.maxsize

    x_min = sys.maxsize
    y_max = -sys.maxsize
    y_min = sys.maxsize
    ip_list = set()
    for s1, s2 in combinations(line, 2):
        tmp = intersection_point(s1, s2)
        if tmp:
            x_max = max(tmp[0], x_max)
            x_min = min(tmp[0], x_min)
            y_max = max(tmp[1], y_max)
            y_min = min(tmp[1], y_min)
            ip_list.add(tmp)
    for i in range(y_min, y_max+1):
        tmp = []
        for j in range(x_min, x_max+1):
            tmp.append('.')
        answer.append(tmp)

    for x, y in ip_list:
        answer[y-y_min][x-x_min] = '*'
    res = []
    for i in range(len(answer)-1, -1, -1):
        res.append(''.join(answer[i]))

    return res
