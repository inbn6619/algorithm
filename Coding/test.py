park = ["SOO","OOO","OOO"]	
routes = ["E 2","S 2","W 1"]

t1 = ["SOO","OXX","OOO"]	
t11 =["E 2","S 2","W 1"]	

t2 =["OSO","OOO","OXO","OOO"]	
t22 =["E 2","S 3","W 1"]	

def check(num, length, i, state):
    a = num + i
    c = num - i
    b = length
    if not state:
        a, b = c, b

    if a > b:
        return 0
    else:
        return i
    
def solution(park, routes):
    x, y = 0, 0

    for i in range(len(park)):
        if park[i] in 'S':
            x, y = i, i.find('S')

    routes = [i.split(' ') for i in routes]
    width = len(park[0])
    heigth = len(park)

    for way, i in routes:
        i = int(i)
        if way == 'E':
            y += check(y, width, i, True)
        if way == 'S':
            x += check(x, heigth, i, True)
        if way == 'W':
            y -= check(y, 0, i, False)
        if way == 'S':
            x -= check(x, 0, i, False)

    answer = [x, y]

    return answer



print(solution(park, routes))#[2,1]
print(solution(t1, t11))#[0,1]
print(solution(t2, t22))#[0,0]