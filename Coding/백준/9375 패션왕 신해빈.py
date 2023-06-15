T = int(input())

for _ in range(T):
    N = int(input())

    cloths = dict()

    for n in range(N):
        cloth, cloth_case = input().split()

        if cloth_case in cloths:
            cloths[cloth_case].append(cloth)
        else:
            cloths[cloth_case] = [cloth]

    count = 1

    for key in cloths:
        count *= (len(cloths[key]) + 1)
    
    print(count - 1)
