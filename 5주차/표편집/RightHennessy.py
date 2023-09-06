def solution(n, k, cmd):

    now = k
    size = n
    stack = []
    stack_count = []
    answer = ['O']*n

    for command in cmd:
        print(stack)
        print(stack_count)
        if command[0] == 'D':
            now += int(command.split(' ')[-1])
        elif command[0] == 'U':
            now -= int(command.split(' ')[-1])
        elif command[0] == 'Z':
            size += 1
            stack_count.pop()
            if stack.pop() <= now:
                now += 1
        elif command[0] == 'C':
            c = 0
            for s in stack:
                if now >= s:
                    c += 1
            stack.append(now)
            size -= 1
            stack_count.append(c)
            if now == size:
                now -= 1

    while stack:
        idx = stack.pop() + stack_count.pop()
        answer[idx] = 'X'

    return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))