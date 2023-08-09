depth = 0


def convert(x: str) -> int:
    global depth
    depth += 1
    if x == '1':
        return 0

    zero_cnt = x.count('0')

    return zero_cnt + convert(bin(int(len(x) - zero_cnt))[2:])


def solution(s):

    answer = convert(s)
    return [depth-1, answer]
