def solution(enroll, referral, seller, amount):
    cnt = len(enroll)
    answer = [0] * (cnt + 1)
    parents = [i for i in range(cnt + 1)]

    info = dict()
    for i in range(cnt):
        info[enroll[i]] = i + 1

    for i in range(cnt):
        if referral[i] == "-":
            parents[i + 1] = 0
        else:
            parents[i + 1] = info[referral[i]]

    def find(parents, money, idx, answer):
        if parents[idx] == idx or money // 10 == 0:
            answer[idx] += money
            return

        fee = money // 10
        alloc_Money = money - fee
        answer[idx] += alloc_Money
        find(parents, fee, parents[idx], answer)

    for i in range(len(seller)):
        find(parents, amount[i] * 100, info[seller[i]], answer)

    return answer[1:]