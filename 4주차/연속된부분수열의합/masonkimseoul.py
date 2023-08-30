def solution(sequence, k):
    answer = []
    sum = 0
    l, r = 0, -1

    while True:
        if sum == k:
            answer.append([l, r])

        if sum < k:
            r += 1
            if r >= len(sequence): break
            sum += sequence[r]

        else:
            sum -= sequence[l]
            if l >= len(sequence): break
            l += 1

    answer.sort(key = lambda x: (x[1] - x[0], x[0]))
    return answer[0]
