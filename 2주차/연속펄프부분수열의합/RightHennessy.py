def solution(sequence):

    seq1 = []
    seq2 = []

    for i in range(0, len(sequence)):
        if i%2==0:
            seq1.append(sequence[i])
            seq2.append(-sequence[i])
        else:
            seq1.append(-sequence[i])
            seq2.append(sequence[i])

    answer = max(calculate(seq1), calculate(seq2))

    return answer

def calculate(seq):
    dp = [0 for _ in range(len(seq))]
    dp[0] = seq[0]

    for i in range(1, len(seq)):
        dp[i] = max(dp[i-1]+seq[i], seq[i])
    return max(dp)