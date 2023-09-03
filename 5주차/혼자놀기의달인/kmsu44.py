# 4시 10분 시작
from collections import deque, defaultdict


def find_group(box, cards, open_box, group_num, group):
    flag = True
    while open_box[box] == 0:
        flag = False
        open_box[box] = group_num
        group[group_num] += 1
        if box != cards[box-1]:
            find_group(cards[box-1], cards, open_box, group_num, group)
    return flag


def solution(cards):
    answer = 0
    group = [0 for _ in range(len(cards)+1)]
    group_num = 1
    open_box = [0 for _ in range(len(cards)+1)]
    for box in cards:
        if find_group(box, cards, open_box, group_num, group):
            continue
        else:
            group_num += 1
    group.sort()

    if len(group) > 2:
        answer = group[-1] * group[-2]

    return answer
