def time_to_min(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def get_notes(notes):
    return notes.replace('C#', 'c').replace('D#', 'd').replace('E#', 'e').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    answer = ('(None)', 0)
    for music in musicinfos:
        start, end, name, notes = music.split(',')
        play_time = time_to_min(end) - time_to_min(start)
        notes = get_notes(notes)
        notes = notes * (play_time // len(notes)) + notes[:play_time % len(notes)]

        if get_notes(m) in notes:
            if answer[1] < play_time:
                answer = (name, play_time)

    return answer[0]

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(get_notes('C#DEFGAB'))