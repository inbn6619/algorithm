def solution(k, dungeons):
    leng = len(dungeons)
    check = [False for _ in range(leng)]
    array = list()

    def dfs(num, cnt):
        

        for i in range(leng):
            if not check[i]:
                n, m = dungeons[i]
                if num >= n:
                    cnt += 1
                    check[i] = True
                    dfs(num - m, cnt)
                    check[i] = False
                    cnt -= 1
        array.append(cnt)
        return

    for i in range(leng):
        if dungeons[i][0] <= k:
            num = k - dungeons[i][1]
            cnt = 1
        else:
            continue
        check[i] = True
        dfs(num, cnt)
        check[i] = False

    answer = max(array)
    return answer

solution(80, [[80,20],[50,40],[30,10]])