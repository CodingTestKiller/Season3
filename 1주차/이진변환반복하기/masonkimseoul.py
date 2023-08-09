def solution(s):
    cnt_zero = 0
    cnt_try = 0

    while s != '1':
        if '0' in s:
            cnt_zero += s.count('0')
            s = s.replace('0', '')
        s = str(bin(len(s)))[2:]
        cnt_try += 1

    return [cnt_try, cnt_zero]