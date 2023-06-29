def solution(genres, plays):
    gen_dict = dict()
    array = list()
    answer = []

    for key, value in zip(genres, plays):
        gen_dict[key] = gen_dict.get(key, 0) + int(value)
    sum_dict = sorted(gen_dict.items(), key=lambda x:x[1], reverse=True)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        array.append([idx, genre, play])

    sort_array = sorted(array, key=lambda x : x[2], reverse=True)

    for genre, _ in sum_dict:
        cnt = 0
        for i in sort_array:
            if cnt == 2:
                break
            if i[1] == genre:
                answer.append(i[0])
                cnt += 1            

    return answer


genres1 = ["classic", "pop", "classic", "classic", "pop"]	
plays1 = [500, 600, 150, 800, 2500]
plays2 = [500, 500, 500, 500, 500]

# print(solution(genres1, plays1))
print(solution(genres1, plays2))