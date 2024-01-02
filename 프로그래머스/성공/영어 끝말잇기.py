def solution(n, words):
    answer = [0, 0]

    m = len(words)//n

    stack = list()

    setList = set()

    for i in range(m):
        for j in range(n):
            a = j + i*n

            word = words[a]

            if word not in setList:
                setList.add(word)
                if stack:
                    if stack[-1][-1] != word[0]:
                        return [j+1, i+1]

                stack.append(word)

                    
            else:
                return [j+1, i+1]

    return answer