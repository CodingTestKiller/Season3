
import math


def solution(r1, r2):
    answer = 0
    for x in range(1, r2):
        h2 = math.sqrt(r2*r2-x*x)
        h1 = math.sqrt(r1*r1-x*x)

        answer += int(h2-h1+1)
    answer *= 4

    return answer


print(solution(2, 3))
