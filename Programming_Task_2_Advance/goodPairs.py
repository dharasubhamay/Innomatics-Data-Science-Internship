#https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums):
        cnt = 0
        for idx in range(len(nums)):
            for id in range(idx, (len(nums))):
                if(nums[idx] == nums[id] and idx < id):
                  cnt += 1
        return cnt

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))