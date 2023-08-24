# 1시 30분 시작
def timeconversion(time):
    hour = int(time[0:2])
    minute = int(time[3:])
    return hour*60+minute


def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    progress = []

    prevstart = 0
    for name, start, during in plans:
        start = timeconversion(start)
        during = int(during)
        end = start+during

        # 중간에 있었던 시간
        time = start - prevstart
        prevstart = start
        # 끝난 친구들이 있는지?
        while progress and time > 0:
            pend, pduring, pname = progress.pop()
            if pduring <= time:
                time -= pduring
                answer.append(pname)
            else:
                pduring -= time
                progress.append((pend, pduring, pname))

                break
        progress.append((end, during, name))

    while progress:
        end, during, name = progress.pop()

        answer.append(name)
    return answer
