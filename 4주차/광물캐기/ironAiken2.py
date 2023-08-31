def solution(picks, minerals):
    tired = []
    p = 0
    for _ in range(sum(picks)):
        d, i, s = 0, 0, 0
        for _ in range(5):
            if p >= len(minerals):
                break
            if minerals[p] == "diamond":
                d += 1
            elif minerals[p] == "iron":
                i += 1
            else:
                s += 1
            p += 1
        tired.append([d, i, s])
        if p >= len(minerals):
                break
                
    answer = 0
    tired.sort(key=lambda x:[x[0],x[1]])
    print(tired)
    for _ in range(picks[0]):
        answer += sum(tired[-1])
        del tired[-1]
        if not tired:
            return answer

    for _ in range(picks[1]):
        answer += sum(tired[-1][1:3])
        answer += tired[-1][0] * 5
        del tired[-1]
        if not tired:
            return answer
        
    for _ in range(picks[2]):
        answer += tired[-1][2]
        answer += tired[-1][1] * 5
        answer += tired[-1][0] * 25
        del tired[-1]
        if not tired:
            return answer