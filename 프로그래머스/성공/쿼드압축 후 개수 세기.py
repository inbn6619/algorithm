

def solution(arr):
    answer = [0, 0]
    
    def quadTree(matrix):
        ans = list()

        if matrix[0] == 0:
            ans.append(0)
            answer[0] += 1
            return ans
        elif matrix[0] == 1:
            ans.append(1)
            answer[1] += 1
            return ans

        h = len(matrix)
        w = len(matrix[0])


        zeroCheck = True
        oneCheck = True

        for i in range(h):
            for j in range(w):
                if matrix[i][j] != 0:
                    zeroCheck = False
                elif matrix[i][j] != 1:
                    oneCheck = False
        if zeroCheck:
            ans.append(0)
            answer[0] += 1
        elif oneCheck:
            ans.append(1)
            answer[1] += 1
        else:
            ans.append(quadTree([row[:w//2] for row in matrix[:h//2]]))
            ans.append(quadTree([row[w//2:] for row in matrix[:h//2]]))
            ans.append(quadTree([row[:w//2] for row in matrix[h//2:]]))
            ans.append(quadTree([row[w//2:] for row in matrix[h//2:]]))

        return ans
    
    quadTree(arr)
    
    return answer
