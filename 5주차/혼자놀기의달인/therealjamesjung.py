def solution(cards):
    visited = [0] * (len(cards) + 1)
    cards = [0] + cards
    result = []

    index = 1

    while index < len(cards):
        while visited[index]:
            index += 1
            if index == len(cards):
                if len(result) == 1:
                    return 0
                result.sort()
                return result[-1] * result[-2]
        
        tmp = cards[index]
        visited[index] = 1
        cnt = 1

        while tmp != index:
            visited[tmp] = 1
            tmp = cards[tmp]
            cnt += 1
        result.append(cnt)

    if len(result) == 1:
        return 0
    result.sort()
    return result[-1] * result[-2]
        
