def solution(plans):
    for plan in plans:
        a, b = plan[1].split(':')
        plan[1] = int(a) * 60 + int(b)
        plan[2] = int(plan[2])
    plans.sort(key = lambda x:x[1])
    
    answer = []
    waitings = []
    for i in range(len(plans)):
        try:
            remain = plans[i+1][1] - plans[i][1]
        except:
            answer.append(plans[i][0])
            continue
        remain -= plans[i][2]
        if remain < 0:
            waitings.append([plans[i][0], -remain])
            continue
    
        answer.append(plans[i][0])
        while waitings:
            remain -= waitings[-1][1]
            if remain < 0:
                waitings[-1][1] = -remain
                break
            answer.append(waitings[-1][0])
            waitings.pop()
    while waitings:
        answer.append(waitings[-1][0])
        waitings.pop()
              
    
    return answer