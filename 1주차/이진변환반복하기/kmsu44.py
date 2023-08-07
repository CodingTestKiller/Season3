# 9시 30분 시작
def solution(s):
    answer = [0, 0]

    while s != '1':
        tmp = []
        count_one = s.count('1')
        count_zero = s.count('0')
        s = bin(count_one)[2:]
        answer[0] += 1
        answer[1] += count_zero

    return answer
