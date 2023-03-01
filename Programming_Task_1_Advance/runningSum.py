#https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum(nums):
    result = []
    for idx, item in enumerate(nums):
        num = 0
        for i in range(idx+1):
            num += nums[i]
        result.append(num)
    return result

nums = [3,1,2,10,1]
res = runningSum(nums)
print(res)