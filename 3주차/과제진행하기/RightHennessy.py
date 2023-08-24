def solution(plans: list):

    stack = []
    answer = []

    for plan in plans:
        plan[1] = convert(plan[1])
        plan[2] = int(plan[2])

    plans.sort(key = lambda x:x[1])

    for idx in range(0, len(plans)-1):
        nextTime = plans[idx+1][1]
        overTime = plans[idx][1] + plans[idx][2]

        if overTime == nextTime:
            answer.append(plans[idx][0])
        elif overTime > nextTime:
            plans[idx][2] = overTime - nextTime
            stack.append(plans[idx])
        else:
            answer.append(plans[idx][0])
            while stack:
                last = stack.pop()
                overTime += last[2]

                if overTime <= nextTime:
                   answer.append(last[0])
                elif overTime > nextTime:
                    last[2] = overTime - nextTime
                    stack.append(last)
                    break

    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
            
    return answer

def convert(str) -> int:
    time = str.split(':')
    return int(time[0])*60 + int(time[1])
