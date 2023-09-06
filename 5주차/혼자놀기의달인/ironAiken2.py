def visited(cards, i, cnt, ans):
    if cards[i] == -1:
        ans.append(cnt)
        return
    flag = cards[i]
    cards[i] = -1
    visited(cards, flag-1, cnt+1, ans)
def solution(cards):
    ans = []
    for i in range(len(cards)):
        if cards[i] == -1:
            continue
        visited(cards, i, 0, ans)
    
    ans.sort()
    print(ans)
    if len(ans) == 1:
        return 0
    else:
        return ans[-2] * ans[-1]