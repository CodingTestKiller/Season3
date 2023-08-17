import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        y_pos1 = math.sqrt(r2**2 - i**2)
        y_pos2 = 0
        if i <= r1:
            y_pos2 = math.sqrt(r1**2 - i**2)
        answer += math.floor(y_pos1) - math.ceil(y_pos2) + 1

    return answer * 4