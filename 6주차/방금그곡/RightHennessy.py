# 2글자를 1글자로 바꿔주는 IDEA : replace

import math

def solution(m, musicinfos):

    answer = []

    m = convert_code(m)
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        play_time = convert_time(info[0], info[1])
        music = info[2]
        code = convert_code(info[3])

        if len(code) <= play_time:
            code *= math.ceil(play_time / len(code))
        code = code[:play_time]
        
        if m not in code:
            continue
        answer.append([music, play_time])
        
    if len(answer) == 0:
        return '(None)'
    
    return sorted(answer, key = lambda x: x[1], reverse = True)[0][0]

def convert_code(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('E#', 'e').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def convert_time(s1, s2):
    time_s2 = list(map(int, s2.split(':')))
    time_s1 = list(map(int, s1.split(':')))
    return (time_s2[0]*60 + time_s2[1]) - (time_s1[0]*60 + time_s1[1]) 