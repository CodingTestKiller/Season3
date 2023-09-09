def solution(n, k, cmd):
    answer = ['O'] * n
    pointer = [[i - 1,i + 1] for i in range(n)]
    pointer[0] = [None,1]
    pointer[n-1] = [n-2,None]
    trash = []
    for c in cmd:
        if c == "C":
            answer[k] = 'X'
            prv,nxt = pointer[k]
            trash.append([prv,k,nxt])
            if nxt == None:
                k = pointer[k][0]
            else:
                k = pointer[k][1]
            if prv == None:
                pointer[nxt][0] = None
            elif nxt == None:
                pointer[prv][1] = None
            else:
                pointer[prv][1] = nxt
                pointer[nxt][0] = prv
        elif c == "Z":
            prv,cur,nxt = trash.pop()
            answer[cur] = 'O'
            if prv == None:
                pointer[nxt][0] = cur
            elif nxt == None:
                pointer[prv][1] = cur
            else:
                pointer[nxt][0] = cur
                pointer[prv][1] = cur
        else:
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    k = pointer[k][1]
            else:
                for _ in range(c2):
                    k = pointer[k][0]
    return ''.join(answer)