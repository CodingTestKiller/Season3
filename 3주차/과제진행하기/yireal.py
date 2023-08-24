def solution(plans):
    answer = []
    for i in range(len(plans)):
        hour,minute = map(int,plans[i][1].split(':'))
        calc_time = hour * 60 + minute
        plans[i][1] = calc_time
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x : x[1])
    stack = []
    for i in range(len(plans)):
        if i == len(plans) - 1:
            stack.append(plans[i])
            break
        name,sch,t = plans[i]
        n_namx,n_sch,n_t = plans[i+1]
        if sch + t <= n_sch:
            answer.append(name)
            tmp_time = n_sch - (sch + t)
            while tmp_time != 0 and stack:
                t_name,t_sch,t_t = stack.pop()
                if tmp_time >= t_t:
                    answer.append(t_name)
                    tmp_time -= t_t
                else:
                    stack.append([t_name,t_sch,t_t-tmp_time])
                    tmp_time = 0
        else:
            plans[i][2] = t - (n_sch - sch)
            stack.append(plans[i])
    while stack:
        name,sch,t = stack.pop()
        answer.append(name)
                          
                        
                
    return answer