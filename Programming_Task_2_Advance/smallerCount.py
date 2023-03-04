#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent(nums):
    res = []
    for idx in range(len(nums)):
        cnt = 0
        for id in range(len(nums)):
            if(nums[id] < nums[idx]):
                cnt += 1
        res.append(cnt)
    return res

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))