def timeconvert(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


def solution(m, musicinfos):
    data = {
        'C#': 'J',
        'D#': 'K',
        'F#': 'L',
        'G#': 'M',
        'A#': 'N',
        'E#': "T"

    }

    answer = {}
    musicinfos = [info.split(',') for info in musicinfos]
    # musicinfos.sort(key = lambda x : x)

    for info in musicinfos:
        start, end, name, melody = info
        start = timeconvert(start)
        end = timeconvert(end)

        playtime = end - start+1

        cnt = 0
        idx = 0
        idx_next = 1
        size = len(m)
        m_array = []
        for i in m:
            if i == '#':
                t = m_array.pop()
                m_array.append(data[t+i])
            else:
                m_array.append(i)

        result = ''.join(str(s) for s in m_array)

        melody_array = []
        for i in melody:
            if i == '#':
                t = melody_array.pop()
                melody_array.append(data[t+i])
            else:
                melody_array.append(i)

        result_melody = ''
        for i in range(playtime):
            result_melody += melody_array[i % len(melody_array)]

        print(result, result_melody)
        if result in result_melody:
            if answer == {}:
                answer["name"] = name
                answer["playtime"] = playtime
            else:
                if playtime > answer["playtime"]:
                    answer["name"] = name
                    answer["playtime"] = playtime
    if answer == {}:
        answer["name"] = "(None)"

    return answer['name']
