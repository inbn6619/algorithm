house = [int(i) for i in input().replace('9', '6')]

array = [i for i in range(10)]

count = 0

while house:
    count += 1

    for i in array:
        if i == 9:
            i = 6
        if i in house:
            house.remove(i)

print(count)
