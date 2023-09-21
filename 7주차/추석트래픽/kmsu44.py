def solution(lines):
    global min_millisec,targets
    targets = []

    min_millisec,min_t = time_to_millisec(lines[0])

    for line in lines:
        millisec,t = time_to_millisec(line)
        calc_start_end(millisec,t)

    answer = 1

    for i in range(len(targets)-1):
        tmp = 1
        for j in range(i+1,len(targets)):
            if targets[i][1] >= targets[j][0]:
                tmp += 1
            elif targets[i][1] + 999 >= targets[j][0]:
                tmp += 1
        answer = max(answer, tmp)

    return answer

def calc_start_end(millisec,t):
    start = millisec - min_millisec - t + 3001
    end = millisec - min_millisec + 3000

    targets.append((start,end))
def time_to_millisec(line):
    line = line.split()
    millisec = line[1]

    ms = int(millisec[9:])
    s = int(millisec[6:8]) * 1000
    m = int(millisec[3:5]) * 1000 * 60
    h = int(millisec[:2]) * 1000 * 60 * 60
    millisec = ms + s + m + h

    t = int(float(line[2][:-1]) * 1000)

    return millisec,t