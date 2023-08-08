def solution(s):
    answer = []
    ans = 0
    total = 0
    s = list(s)
    while len(s) > 1:
        i = 0
        size = len(s)
        s = list(s)
        while i < size:
            if s[i] == '0':
                s.pop(i)
                total += 1
                size -= 1
            else:
                i += 1
        tmp = list(bin(len(s))[2:])
        s = tmp
        ans += 1
    answer.append(ans)
    answer.append(total)
    return answer