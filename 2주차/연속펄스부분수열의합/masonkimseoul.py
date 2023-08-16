def solution(s):
    answer = -float("inf")

    a1, a2, a1_min, a2_min = 0, 0, 0, 0
    pulse = 1
    for i in range(len(s)):
        a1 += pulse * s[i]
        a2 += -pulse * s[i]
        answer = max(answer, a1 - a1_min, a2 - a2_min)

        a1_min = min(a1_min, a1)
        a2_min = min(a2_min, a2)

        pulse *= -1
    return answer