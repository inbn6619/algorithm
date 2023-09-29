def solution(n):
    target = bin(n).count("1")

    num = n + 1

    while True:
        result = bin(num).count("1")

        if result == target:
            break
        else:
            num += 1
    answer = num
    return answer

print(solution(78))