from collections import deque

def solution(info, query):
    result = []
    for i in range(len(info)):
        info[i] = info[i].split()
    for i in range(len(query)):
        query[i] = query[i].split()
        j = 0
        tmp = len(query[i])
        while j < tmp:
            if query[i][j] == 'and':
                del query[i][j]
                j -= 1
                tmp -= 1
            j += 1
        answer = deque(range(len(info)))

        for k in range(len(query[i])-1):
            cnt=len(answer)
            j=0
            while j<cnt:
                tmp=answer.popleft()
                if query[i][k]!=info[tmp][k] and query[i][k]!='-':
                    j-=1
                    cnt-=1
                else:
                    answer.append(tmp)
                j+=1
        cnt=len(answer)
        j=0
        while j<cnt:
            tmp=answer.popleft()
            if int(info[tmp][4])<int(query[i][4]):
                j-=1
                cnt-=1
            else:
                answer.append(tmp)
            j+=1
        result.append(len(answer))
    return result