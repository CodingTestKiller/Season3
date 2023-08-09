from collections import deque


def solution(s):
    queue = deque()

    for c in s:
        if queue and queue[-1] == c:
            queue.pop()
        else:
            queue.append(c)

    return 1 if not queue else 0
