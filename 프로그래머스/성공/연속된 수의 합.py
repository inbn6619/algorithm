# num % 2 == 0
# num //2 -1 < mid < num // 2
# else:
# num // 2 < mid < num // 2

def solution(num, total):
    mid = total//num
    key = 0

    if num % 2 == 0:
        key += 1

    answer = [int(i) for i in range(mid - num // 2 + key, mid + num //2 + 1)]

    return answer