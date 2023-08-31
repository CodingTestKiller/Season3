# index 찾는게 오래 걸리는거 같아서.. 
# dict의 시간복잡도를 몰라 헤맨 문제.. 하지만 이제 dict 안다는거 ~

import math

def solution(enroll, referral, seller, amount):
    global answer
    answer = [0 for _ in range(len(enroll))]

    global enrolls
    enrolls = dict()
    for idx, e in enumerate(enroll):
        enrolls[e] = idx

    global referrals
    referrals = referral

    for idx, s in enumerate(seller):
        calculate(s, amount[idx]*100)

    return answer

def calculate(name, revenue):
    
    idx = enrolls[name]
    charge = math.floor(revenue*0.1)
    revenue -= charge
    answer[idx] += revenue

    if charge == 0:
        return
    
    if referrals[idx] == '-':
        return
    else:
        calculate(referrals[idx], charge)