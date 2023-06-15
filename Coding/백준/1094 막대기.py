array = [64]

X = int(input())

while sum(array) != X:
    if max(array) > X:
        stick = array.pop(array.index(max(array)))//2
        if stick < X:
            array.append(stick)
        array.append(stick)

    else:
        stick = array.pop()//2

        if sum(array) + stick < X:
            array.append(stick)
        array.append(stick)

print(len(array))