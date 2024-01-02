def solution(nums):
    answer = 0
    
    numList = list()

    for i in range(len(nums)-2):
        for j in range(i + 1, len(nums)-1):
            for k in range(j + 1, len(nums)):
                numList.append(nums[i] + nums[j] + nums[k])
    
    print(numList)
    
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                return False
        return True
    
    for n in numList:
        if is_prime(n):
            answer += 1
    
    
    return answer