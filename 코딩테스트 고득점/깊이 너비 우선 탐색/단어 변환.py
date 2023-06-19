def solution(begin, target, words):
 
    visited = list()
    answer = 0
    
    def check(a, b):
        n = len(a)
        cnt = 0

        for i in range(n):
            if a[i] == b[i]:
                cnt += 1
        
        if cnt + 1 == n:
            return True
        return False


    def dfs(begin, target, node):
        visited.append(node)

        if target == node:
            nonlocal answer
            answer = len(visited)
            return

        for word in words:
            if word not in visited and check(node, word):
                dfs(node, target, word)
                visited.pop()


    for w in words:
        if check(begin, w):
            dfs(begin, target, w)



    
    return answer

words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
words2 = ["hot", "dot", "dog", "lot", "log"]

print(solution("hit", "cog", words1)) # 4
print(solution("hit", "cog", words2)) # 0