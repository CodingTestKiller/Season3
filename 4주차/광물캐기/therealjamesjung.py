def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def get_pick(picks):
    if picks[0] > 0:
        picks[0] -= 1
        return 'diamond'
    elif picks[1] > 0:
        picks[1] -= 1
        return 'iron'
    elif picks[2] > 0:
        picks[2] -= 1
        return 'stone'

def solution(picks, minerals):
    minerals = batch(minerals, 5)
    tmp = []

    for mineral in minerals:
        current = [0, 0, 0, 0]
        for m in mineral:
            if m == 'diamond':
                current[0] += 1
            elif m == 'iron':
                current[1] += 1
            elif m == 'stone':
                current[2] += 1
        
        current[3] = current[0] * 25 + current[1] * 5 + current[2]
        tmp.append(current)
    
    tmp = tmp[:sum(picks)]
    tmp.sort(key=lambda x: -x[3])

    result = 0

    for mineral in tmp:
        pick = get_pick(picks)
        if pick == 'diamond':
            result += mineral[0] + mineral[1] + mineral[2]
        elif pick == 'iron':
            result += mineral[0] * 5 + mineral[1] + mineral[2]
        elif pick == 'stone':
            result += mineral[0] * 25 + mineral[1] * 5 + mineral[2]

    return result
