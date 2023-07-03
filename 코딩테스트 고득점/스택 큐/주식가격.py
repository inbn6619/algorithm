def solution(prices):
    answer = [0 for _ in range(len(prices))]
    st = [0]
    for i in range(1,len(prices)): # 스택에 쌓은 건 아직 언제 떨어질지 모르는 시간들
        while st and prices[st[-1]] > prices[i]:
            prev = st[-1]
            answer[prev] = i-prev
            st.pop()
        st.append(i)

    for sec in st:
        answer[sec] = i - sec
    return answer

# print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
# print(solution([2, 2, 3, 1, 5])) # [3, 2, 1, 1, 0]
# print(solution([1, 2, 3, 4, 1] )) #  [4, 3, 2, 1, 0]
# print(solution([5, 4, 3, 2, 5])) # [1, 1, 1, 1, 0]
# print(solution([1, 2, 3, 2, 3, 1])) # [5, 4, 1, 2, 1, 0]
print(solution([3, 4, 5, 3, 4, 1]))