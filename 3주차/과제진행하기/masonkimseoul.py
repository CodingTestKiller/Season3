def solution(plans):
    answer = []
    stack = []

    for task in plans:
        h, m = map(int, task[1].split(':'))
        task[1] = h * 60 + m
        task[2] = int(task[2])

    plans.sort(key = lambda x : x[1])

    for i in range(len(plans)):
        ETA = plans[i][1] + plans[i][2]

        if i == len(plans) - 1:
            answer.append(plans[i][0])
        else:
            next_task_start = plans[i + 1][1]

            if ETA > next_task_start:
                plans[i][2] -= next_task_start - plans[i][1]
                stack.append([plans[i][0], plans[i][2]])
            else:
                answer.append(plans[i][0])

                zzam = next_task_start -ETA

                if zzam > 0 and stack:
                    while zzam > 0 and stack:
                        tmp = stack.pop(-1)
                        if tmp[1] <= zzam:
                            answer.append(tmp[0])
                            zzam -= tmp[1]
                        else:
                            tmp[1] -= zzam
                            zzam = 0
                            stack.append(tmp)
    while stack:
        answer.append(stack.pop()[0])

    return answer