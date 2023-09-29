def solution(quiz):
    answer = []

    for q in quiz:
        check = True
        xy, z = q.split(' = ')
        if ' - ' in xy:
            x, y = xy.split(' - ')
            check = False
        else:
            x, y = xy.split(' + ')

        x, y, z = [int(i) for i in [x, y, z]]

        res = 0

        if check:
            res = x + y
        else:
            res = x - y
        
        if res == z:
            answer.append('O')
        else:
            answer.append('X')


    return answer