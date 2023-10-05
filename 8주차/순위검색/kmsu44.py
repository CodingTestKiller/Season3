# 9시 30분
from bisect import bisect_left, bisect_right
def solution(info, query):
    answer = []
    info_list = [i.split() for i in info]
    
    info_list.sort(key=lambda x: int(x[4]))    
    D = {}
    language_list = ['cpp','python','java','-']
    major_list = ['frontend','backend','-']
    carrer_list = ['junior', 'senior','-']
    food_list = ['pizza', 'chicken','-']
    for language in language_list:
        for major in major_list:
            for career in carrer_list:
                for food in food_list:
                    D[(language,major,career,food)] = []
    
    for l,m,c,f,score in info_list:
        for q,w,e,r in D:
            if q == l or q =='-':
                if w ==m or w=='-':
                    if e ==c or e=='-':
                        if r ==f or r=='-':
                            D[(q,w,e,r)].append(int(score))

    for q in query:
        a,b,c,d = q.split(' and ')
        d,e = d.split()
        score = int(e)
        
        answer.append(len(D[(a,b,c,d)])- bisect_left(D[(a,b,c,d)],score))
        
        
        
        
        
    return answer