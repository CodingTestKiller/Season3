def solution(sequence):
    purse = [-1 if i%2 == 0 else 1 for i in range(len(sequence))]    
    purse_reverse = [(val * -1) for val in purse]
    seq1 = [x*y for x, y in zip(sequence, purse)]
    seq2 = [x*y for x, y in zip(sequence, purse_reverse)]
    
    dp1, dp2 = [0] * len(sequence), [0] * len(sequence)
    dp1[0], dp2[0] = seq1[0], seq2[0]
    
    for i in range(1, len(sequence)):
        dp1[i] = max(seq1[i], seq1[i] + dp1[i-1])
        dp2[i] = max(seq2[i], seq2[i] + dp2[i-1])
    
    ans = max(max(dp1), max(dp2))
    
    return ans