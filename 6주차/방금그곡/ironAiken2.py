def solution(m, musicinfos):
    m = list(m)
    for i in range(len(m)):
        if m[i] == "#":
            m[i-1] = chr(ord(m[i-1]) + 32)
    m = "".join(m)

    ans, ans_name = 0, "(None)"
    for data in musicinfos:
        start, end, name, code = data.split(',')
        code = list(code)
        for i in range(len(code)):
            if code[i] == "#":
                code[i-1] = chr(ord(code[i-1]) + 32)
        code = "".join(code)

        h, boon = start.split(':')
        start = int(h) * 60 + int(boon)
        h, boon = end.split(':')
        end = int(h) * 60 + int(boon)
        total_play = end - start

        quotient, remain = total_play // len(code), total_play % len(code)
        full_content = code * quotient + code[:remain]

        if m in full_content:
            if ans < total_play:
                ans = total_play
                ans_name = name
    return ans_name
