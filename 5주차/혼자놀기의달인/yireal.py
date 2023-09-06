def solution(cards):
    answer = 0
    deck_size = len(cards)
    cnt = [0] * (deck_size + 1)
    visit = [False] * (deck_size + 1)
    for i in range(1,deck_size + 1):
        cur = i
        while not visit[cur]:
            cnt[i] += 1
            visit[cur] = True
            cur = cards[cur-1]
        if cnt[i] == deck_size:
            return 0
    cnt.sort()
    print(cnt)

    answer = cnt[-1] * cnt[-2]
        
        
            
    
    return answer