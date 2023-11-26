def solution(t, p):
    TLEN = len(t)
    PLEN = len(p)
    answer = 0

    for i in range(TLEN - PLEN + 1):
        n = int(t[i : i + PLEN])
        if n <= int(p):
            answer += 1
    return answer