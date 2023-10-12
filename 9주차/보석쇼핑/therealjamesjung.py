from collections import deque


def solution(gems):
    total_gems = set(gems)
    current_gems = {gem: 0 for gem in total_gems}
    
    l, r = 0, -1
    s, e = 0, len(gems)-1
    bag = deque([])
    
    cnt = 0
    while True:
        r += 1
        bag.append(gems[r])
        if current_gems[gems[r]] == 0:
            cnt += 1
        current_gems[gems[r]] += 1
        if cnt == len(total_gems):
            break

    flag = False
    
    while True:
        if not flag:
            tmp = bag.popleft()
            current_gems[tmp] -= 1
            if current_gems[tmp] == 0:
                flag = True
                if r - l < e - s:
                    s, e = l, r
                elif r - l == e - s and l < s:
                    s, e = l, r
            l += 1
        else:
            if r >= len(gems) - 1:
                break
            r += 1
            bag.append(gems[r])
            current_gems[gems[r]] += 1
            if current_gems[gems[r]] == 1:
                flag = False

    return s+1, e+1
