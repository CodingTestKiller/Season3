
def time_to_minutes(time) -> int:
    hour, minute = [int(x) for x in time.strip().split(':')]
    return hour * 60 + minute

def solution(plans):
    for plan in plans:
        plan[1] = time_to_minutes(plan[1])
        plan[2] = int(plan[2])
    plans.sort(key=lambda x: x[1])

    result = []
    queue = []
    for plan in plans:
        if not queue:
            queue.append(plan)
        else:
            if queue[-1][1] + queue[-1][2] > plan[1]:
                queue[-1][2] -= plan[1] - queue[-1][1]
            elif queue[-1][1] + queue[-1][2] == plan[1]:
                finished = queue.pop()[0]
                result.append(finished)
            else:
                remaining_time = plan[1] - queue[-1][1]
                while queue:
                    if queue[-1][2] > remaining_time:
                        queue[-1][2] -= remaining_time
                        break
                    elif queue[-1][2] == remaining_time:
                        finished = queue.pop()[0]
                        result.append(finished)
                        break
                    else:
                        remaining_time -= queue[-1][2]
                        finished = queue.pop()[0]
                        result.append(finished)
            queue.append(plan)
            
    while queue:
        finished = queue.pop()
        result.append(finished[0])
    return result

a = solution([["s", "12:40", "50"], ["m", "12:20", "40"], ["h", "14:00", "30"], ["c", "12:30", "100"]])
print(a)