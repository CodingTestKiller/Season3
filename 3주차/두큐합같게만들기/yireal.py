from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    default_len = len(queue1)
    i1 = 0
    i2 = 0
    while sum1 != sum2:
        if i1 > default_len and i2 > default_len:
            return -1
        if sum1 > sum2:
            tmp = q1.popleft()
            sum1 -= tmp
            q2.append(tmp)
            sum2 += tmp
            answer += 1
            i1 += 1
        else:
            tmp = q2.popleft()
            sum2 -= tmp
            q1.append(tmp)
            sum1 += tmp
            answer += 1
            i2 += 1
    
    
    return answer