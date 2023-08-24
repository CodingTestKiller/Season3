from collections import deque

def solution(queue1, queue2):
    q1, q2 = sum(queue1), sum(queue2)
    total = q1 + q2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    if total //2 < max(queue1) or total // 2 < max(queue2) or total % 2 != 0:
        return -1
    
    answer = 0
    while q1 != q2:
        if answer == len(queue1) * 4:
            return -1
        if q1 < q2:
            v = queue2.popleft()
            queue1.append(v) 
            q1 += v
            q2 -= v
            answer += 1
        else:
            v = queue1.popleft()
            queue2.append(v)
            q1 -= v
            q2 += v
            answer += 1
    
    return answer