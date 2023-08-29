def buildgraph(referral, graph):
    for idx, name in enumerate(referral):
        if name == '-':
            continue
        else:
            graph[idx] = name


def distribution(seller_list, amount_list, name_list, graph):
    result = [0 for _ in name_list]
    for idx, seller in enumerate(seller_list):
        profit = amount_list[idx] * 100
        distribution_profit = int(profit * 0.1)
        real_profit = profit-distribution_profit
        result[name_list[seller]] += real_profit
        while distribution_profit > 0 and graph[name_list[seller]] != '':

            seller = graph[name_list[seller]]
            profit = distribution_profit
            distribution_profit = int(profit * 0.1)
            real_profit = profit-distribution_profit
            result[name_list[seller]] += real_profit
    return result


def solution(enroll, referral, seller, amount):
    answer = []
    name_list = {}
    for idx, name in enumerate(enroll):
        name_list[name] = idx
    name_list['-'] = len(enroll)
    graph = ['' for _ in range(len(enroll) + 1)]
    buildgraph(referral, graph)

    answer = distribution(seller, amount, name_list, graph)
    answer.pop()

    return answer
