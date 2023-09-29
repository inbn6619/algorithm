def solution(s):
    lst = s.split(" ")
    result = list()
    for i in lst:
        if i:
            result.append(i[0].upper() +  i[1:].lower())
        else:
            result.append(i)
    return " ".join(result)
print(solution("3people unFollowed me"))