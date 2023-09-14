def solution(m, musicinfos):
    m = m.replace("A#", "a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
    answer = {'time': 0, 'name': '(None)'}

    for info in musicinfos:
        s, e, name, cord = info.split(',')
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        playtime = (eh - sh) * 60 + (em - sm)

        cord = cord.replace("A#", "a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
        cord = cord * max(1, int(playtime / len(cord)) + 1)
        cord = cord[:playtime]

        if (m in cord) and (answer['time'] < playtime):
            answer = {'time': playtime, 'name': name}

    return answer['name']