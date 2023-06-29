def solution(clothes):
    clothdict = dict()
    answer = 1

    for key in clothes:
        clothdict[key[-1]] = 0

    for value in clothes:
        clothdict[value[-1]] += len(value[:-1])

    for val in clothdict.values():
        answer = (val + 1) * answer

    return answer