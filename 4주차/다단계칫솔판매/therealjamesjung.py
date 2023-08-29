enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def solution(enroll, referral, seller, amount):
    answer = []

    tree = {}

    for e, r in zip(enroll, referral):
        tree[e] = [r, 0]

    for s, a in zip(seller, amount):
        profit = a * 100
        while s != '-':
            tree[s][1] += profit - profit // 10
            s = tree[s][0]
            profit //= 10
            if profit < 1:
                break

    for e in enroll:
        answer.append(tree[e][1])
    
    return answer


print(solution(enroll, referral, seller, amount))