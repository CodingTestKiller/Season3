def solution(sequence):
    answer = 0
    size = len(sequence)
    # 0 => 1, 1 => -1
    tmp0_list = [0 for _ in range(size)]
    tmp1_list = [0 for _ in range(size)]

    tmp0 = sequence[0]
    if tmp0 < 0:
        tmp0 = 0
    tmp1 = sequence[0] * -1
    if tmp1 < 0:
        tmp1 = 0

    tmp0_list[0] = tmp0
    tmp1_list[0] = tmp1
    for idx in range(1, size):
        # 0번
        tmp0 = tmp1_list[idx-1] + sequence[idx]
        if tmp0 < 0:
            tmp0 = 0
        tmp0_list[idx] = tmp0
        # 1번
        tmp1 = tmp0_list[idx-1] + (-1 * sequence[idx])
        if tmp1 < 0:
            tmp1 = 0
        tmp1_list[idx] = tmp1

    answer = max(max(tmp0_list), max(tmp1_list))

    return answer
