def solution(name):
    if set(name) == {'A'}:
        return 0     
    
    answer = float('inf')
    namelen = len(name)
    num = sum([min(ord(n) - 65, 91 - ord(n))  for n in name])

    for i in range(1, namelen // 2 + 1):
        l_r = name[-i:][::-1] + name[-i:][::-1][:i-1][::-1] + name[:-i]
        r_l = name[:i] + name[:i-1][::-1] + name[i:][::-1] 

        for n in [l_r, r_l]:
            while n and n[-1] == "A":
                n = n[:-1]

            answer = min(answer, len(n) - 1)

    answer = min(answer, namelen) + num
    return answer


print(solution("ABCDEFGHIJKMNLOPQRSTUWYZ"))
print(solution("ABBAAAABBA")) # 6 + n
print(solution("JAN")) # 3 + n
print(solution("JAZ")) # 3 + n
print(solution("JEROEN")) # 6 + n

# ABAAAAAAABABAAA
# AB AAAAAAABABAAA

# !BAAAABAB AAAAAAA
# !AAABABABAAAABA AAAAAAA
