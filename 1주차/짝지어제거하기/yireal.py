def solution(s):
    from collections import deque
    i = 0
    s = list(s)
    q = deque()
    for i in s:
        if q and q[-1] == i:
            q.pop()
        else:
            q.append(i)
    if q:
        return 0
    else:
        return 1