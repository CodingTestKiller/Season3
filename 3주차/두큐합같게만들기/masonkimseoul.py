from collections import deque
def solution(queue1, queue2):
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)

    while sum1 != sum2:
        if answer > (len(q1) + len(q2)) * 2: return -1

        if sum1 < sum2:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        elif sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        answer += 1

    return answer