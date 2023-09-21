def solution(lines):
    answer = 0

    start_log = []
    end_log = []
    for line in lines:
        _, end_time, exce_time = line.split(' ')
        end_log.append(convert_to_time(end_time))
        start_log.append(convert_to_start_time(end_log[-1], exce_time[:-1]))

    for i in range(len(lines)) :
        count = 0
        for j in range(i, len(lines)):
            # 이걸 떠올리는게 힘드네..
            if end_log[i] > start_log[j] - 1000:
                count += 1
        answer = max(answer, count)

    return answer

def convert_to_start_time(end_time, exec_time):
    return end_time - int(float(exec_time)*1000) + 1

def convert_to_time(str):
    return (int(str[:2])*60*60 + int(str[3:5])*60 + int(str[6:8]))*1000 + int(str[9:])