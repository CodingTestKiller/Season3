# 문제를 꼼꼼히 읽자 제발 ~

def solution(cards):

    n = len(cards) + 1
    visited = [False]*n
    cards = [0] + cards
    answers = []

    for i in range(1, n):
        if visited[i] == True:
            continue
        count = 0
        tmp = 0
        while i != tmp:
            if count == 0:
                tmp = i
            tmp = cards[tmp]
            count += 1
            visited[tmp] = True
        answers.append(count)

    answers.sort(reverse=True)
    
    if len(answers)==1:
        return 0
    return answers[0]*answers[1]