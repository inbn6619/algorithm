def solution(numbers):
    check = [False for _ in range(len(numbers))]
    array = list()

    def is_prime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def dfs(num):
        for i in range(len(numbers)):
            if not check[i]:
                if len(num + numbers[i]) > len(numbers):
                    return
                if num + numbers[i] not in array:
                    array.append(num + numbers[i])
                    check[i] = True
                    dfs(num + numbers[i])
                    check[i] = False

    
    for i in range(len(numbers)):
        array.append(numbers[i])
        check[i] = True
        dfs(numbers[i])
        check[i] = False

    array = set([int(i) for i in array])

    cnt = 0

    for i in array:
        if i < 2:
            continue
        if is_prime(i):
            cnt += 1

    answer = cnt
    return answer

solution('17')
solution('011')