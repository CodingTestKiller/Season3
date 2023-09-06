def time_refactor(time):
    return int(time[0:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:])

def solution(play_time, adv_time, logs):
    play_time = time_refactor(play_time)
    adv_time = time_refactor(adv_time)
    dp = [0] * (play_time + 1)

    for log in logs:
        s, e = map(time_refactor, log.split("-"))
        dp[s] += 1
        dp[e] -= 1

    for i in range(2):
        for j in range(1, len(dp)):
            dp[j] += dp[j - 1]

    max_viewer = 0
    max_viewing_time = 0

    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if max_viewer < dp[i] - dp[i - adv_time]:
                max_viewer = dp[i] - dp[i - adv_time]
                max_viewing_time = i - adv_time + 1
        else:
            if max_viewer < dp[i]:
                max_viewer = dp[i]
                max_viewing_time = i - adv_time + 1

    H = max_viewing_time // 3600
    M = max_viewing_time // 60 % 60
    S = max_viewing_time % 60
    if H < 10:
        H = '0' + str(H)
    if M < 10:
        M = '0' + str(M)
    if S < 10:
        S = '0' + str(S)

    return str(H) + ":" + str(M) + ":" + str(S)
