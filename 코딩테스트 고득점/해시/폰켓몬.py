def solution(nums):
    n = len(nums)//2
    hashdict = dict()

    for num in nums:
        hashdict[hash(num)] = nums.count(num)

    if n >= len(hashdict.keys()):
        answer = len(hashdict.keys())
    else:
        answer = n

    return answer

nums1 = [3,1,2,3]
nums2 = [3,3,3,2,2,4]
nums3 = [3,3,3,2,2,2]

print(solution(nums1))
print(solution(nums2))
print(solution(nums3))