def solution(sizes):
    w, h = 0, 0
    for size in sizes:
        a, b = size
        if a < b:
            a, b = b, a

        if w < a:
            w = a
        if h < b:
            h = b

    answer = w * h
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])