import sys


def Area(a, b, middle):
    if a <= middle and b <= middle:
        return 1
    elif a > middle and b > middle:
        return 3
    else:
        return 2


def solution(queue1, queue2):

    answer = sys.maxsize

    memo = [0 for _ in range(len(queue1) * 2 + 1)]
    L = queue1 + queue2

    res = sum(L)
    if res % 2 == 0:
        res = res//2

    else:
        return -1

    for i in range(1, len(L)+1):
        memo[i] = memo[i-1] + L[i-1]

    start, end = 0, 1
    tmp = 0
    tt = []

    flag = False
    while True:
        # print(start,end)
        # print('memo',memo[start],memo[end])
        if end >= len(L)+1 or start >= len(L)+1:
            break
        tmp = memo[end]-memo[start]
        if tmp > res:
            start += 1
        elif tmp == res:
            flag = True
            tt.append((start+1, end))
            start += 1
        else:
            end += 1
    if not flag:
        return -1
    q1_s = 1
    q1_e = len(L)//2
    q2_s = q1_e+1
    q2_e = len(L)

    print('q1_s', q1_s, 'q1_e', q1_e, 'q2_s', q2_s, 'q2_e', q2_e)
    for a, b in tt:
        print(a, b)
        if a == q1_s and b == q1_e or a == q2_s and b == q2_e:
            return 0
        tmp = 0
        area = Area(a, b, len(L)//2)
        print('middle', len(L)//2, 'area', area)

        # 오른쪽에만 있을 때
        if area == 3:
            # 큐의 마지막에 있을 때
            if q2_e == b:
                tmp = a-q2_s
            # 큐의 마지막이 아닐 때
            else:
                # 왼쪽으로 덩어리 옮기기
                tmp += b-q2_s+1
                # 오른쪽으로 왼쪽꺼 옮기기
                tmp += q1_e
                # 남는 덩어리 옮기기
                tmp += a-q2_s

        # 둘사이에 있을 때
        elif area == 2:
            # 오른쪽꺼 왼쪽에 붙이기
            tmp += b - q2_s + 1
            # 왼쪽에 남는거 오른쪽에 붙이기
            tmp += a - q1_s

        # 왼쪽에만 있을 때

        else:
            # 마지막과 같을 때
            if q1_e == b:
                tmp = a-q1_s
            else:
                # 앞에줄 다 오른쪽으로 옮기기
                tmp += b
                # 뒤에거 다 왼쪽으로 붙이기
                tmp += q2_e - q2_s + 1
                # 아닌부분도 넘겨주기
                tmp += a-q1_s
        print('tmp', tmp)

        answer = min(answer, tmp)
    return answer
