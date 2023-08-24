from collections import deque

def solution(queue1: list, queue2: list):

    answer = 0
    maxCount = len(queue1)*2
    sum1, sum2 = sum(queue1), sum(queue2)
    que1, que2 = deque(queue1), deque(queue2)

    while sum1 != sum2:

        if not que1 or not que2 or answer > maxCount:
            return -1

        answer+=1
        if sum1 > sum2:
            tmp = que1.popleft()
            que2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        elif sum1 < sum2:
            tmp = que2.popleft()
            que1.append(tmp)
            sum2 -= tmp
            sum1 += tmp

    return answer