from collections import deque

def solution(s):
    answer = 1
    cnt = 0
    if len(s) % 2 ==1: return 0
    q = deque()

    for i in range(len(s)):
        if q and q[-1] == s[i]: q.pop()
        else: q.append(s[i])

    if q: answer = 0

    return answer