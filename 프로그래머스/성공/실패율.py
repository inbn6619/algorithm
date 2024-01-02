def solution(N, stages):
    answer = []

    s = [0] * N

    for p in stages:
        if p == N + 1:
            continue
        else:
            s[p-1] += 1


    length = len(stages)

    dict_s = dict()


    for j in range(len(s)):
        target = s[j]

        if length > 0:
            dict_s[j + 1] = target/length
        else:
            dict_s[j + 1] = 0
        length = length- target

    sorted_s = sorted(dict_s.items(), key=lambda x : (x[1], -x[0]), reverse=True)

    answer = [item[0] for item in sorted_s]

    return answer