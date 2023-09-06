def solution(n, k, cmd):
    data = {i: [i - 1, i + 1] for i in range(1, n)}
    data[0] = [n - 1, 1]
    data[n - 1] = [n - 2, 0]
    pos = k
    stack = []

    for c in cmd:
        if c == 'C':
            prev, next = data[pos]
            data[prev][1] = next
            data[next][0] = prev

            stack.append([pos, data[pos]])
            del data[pos]
            if next < pos:
                pos = prev
            else:
                pos = next
        elif c == 'Z':
            tmp, elem = stack.pop()
            data[tmp] = elem
            prev, next = elem
            data[prev][1] = tmp
            data[next][0] = tmp
        else:
            opt, step = c.split()
            step = int(step)

            if opt == 'U':
                for _ in range(step):
                    pos = data[pos][0]
            else:
                for _ in range(step):
                    pos = data[pos][1]
    answer = ""
    for i in range(n):
        if i in data:
            answer += 'O'
        else:
            answer += 'X'
    return answer