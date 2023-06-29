def solution(participant, completion):
    hashdict = dict()
    sumhash = 0

    for part in participant:
        hashdict[hash(part)] = part
        sumhash += hash(part)

    for comp in completion:
        sumhash -= hash(comp)


    answer = hashdict[sumhash]
    return answer

participant1 = ["leo", "kiki", "eden"]	
participant2 = ["mislav", "stanko", "mislav", "ana"]	
participant3 = ["marina", "josipa", "nikola", "vinko", "filipa"]

completion1 = ["eden", "kiki"]
completion2 = ["stanko", "ana", "mislav"]
completion3 = ["josipa", "filipa", "marina", "nikola"]
# print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))