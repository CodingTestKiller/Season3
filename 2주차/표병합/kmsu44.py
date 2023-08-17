from collections import deque


class Node:
    def __init__(self, data):
        self.data = data


value_list = [[Node("EMPTY") for _ in range(51)] for _ in range(51)]


def check(r, c):
    if 1 <= r <= 50 and 1 <= c <= 50:
        return True
    else:
        return False


def update_pos(r, c, value):
    if check(r, c) == False:
        return
    value_list[r][c].data = value


def update_value(value1, value2):
    for i in range(1, 51):
        for j in range(1, 51):
            if value_list[i][j].data == value1:
                value_list[i][j].data = value2


def merge(r1, c1, r2, c2):
    if check(r1, c1) == False:
        return
    if check(r2, c2) == False:
        return
    if r1 == r2 and c1 == c2:
        return
    change_list = []
    if value_list[r1][c1].data == 'EMPTY' and value_list[r2][c2] == 'EMPTY':
        value_list[r2][c2] = value_list[r1][c1]
        return
    if value_list[r1][c1].data == 'EMPTY':
        value_list[r1][c1] = value_list[r2][c2]
    else:
        node = value_list[r2][c2]
        for i in range(1, 51):
            for j in range(1, 51):
                if value_list[i][j] == node:
                    change_list.append((i, j))
        for i, j in change_list:
            value_list[i][j] = value_list[r1][c1]


def unmerge(r, c):
    if check(r, c) == False:
        return
    node = value_list[r][c]
    tmp = node.data
    change_list = []
    for i in range(1, 51):
        for j in range(1, 51):
            if value_list[i][j] == node:
                change_list.append((i, j))
    for i, j in change_list:
        value_list[i][j] = Node("EMPTY")
    value_list[r][c] = Node(tmp)


def solution(commands):
    answer = []
    for c in commands:
        command_list = c.split()
        command = command_list[0]
        print(c)
        if command == 'UPDATE':
            # update_pos
            if len(command_list) == 4:
                r, c, v = int(command_list[1]), int(
                    command_list[2]), command_list[3]
                update_pos(r, c, v)
            # update_value
            else:
                v1, v2 = command_list[1:]
                print(v1, v2)
                update_value(v1, v2)
        elif command == 'MERGE':
            r1, c1, r2, c2 = map(int, command_list[1:])
            merge(r1, c1, r2, c2)
        elif command == 'UNMERGE':
            r, c = map(int, command_list[1:])
            unmerge(r, c)
        elif command == "PRINT":

            r, c = map(int, command_list[1:])
            answer.append(value_list[r][c].data)
        for i in range(1, 5):
            for j in range(1, 5):
                print(value_list[i][j].data, end=' ')
            print()
        print("--")

    return answer
