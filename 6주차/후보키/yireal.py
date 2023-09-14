from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    comb = []
    for i in range(1,col+1):
        comb.extend(combinations(range(col),i))
    dup_check = []
    for c in comb:
        tmp = [tuple([line[x] for x in c]) for line in relation]
        if len(set(tmp)) == row:
            flag = True
            for x in dup_check:
                if set(x).issubset(set(c)):
                    flag = False
                    break
            if flag:
                dup_check.append(c)
                    
    return len(dup_check)