def compare(prev_length, now_length):
    if now_length < prev_length:
        return True
    else:
        return False


def solution(sequence, k):
    answer = [-1, len(sequence)]
    prev_start = 0
    prev_end = 0
    start = 0
    end = 0
    flag = True
    size = len(sequence)-1
    sequence = sequence + [0]
    tmp = sequence[start]
    while start <= end and end <= size and start <= size:
        if tmp == k and compare(answer[1]-answer[0], end-start):

            answer[0] = start
            answer[1] = end
        prev_start = start
        prev_end = end

        if tmp == k:
            end += 1
            start += 1
        elif tmp < k:
            end += 1
        else:
            start += 1
        if prev_start != start and start <= size:
            tmp -= sequence[prev_start]
            if tmp < 0:
                tmp = 0
        if prev_end != end and end <= size:
            tmp += sequence[end]

    return answer
