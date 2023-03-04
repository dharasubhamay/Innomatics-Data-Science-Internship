# https://leetcode.com/problems/subsets/

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.calc(result, nums, [], 0)
        return result
    
    def calc(self, result, nums, subset, start):
        result.append(list(subset))
        for i in range(start, len(nums)):
            num = nums[i]
            subset.append(num)
            self.calc(result, nums, subset, i + 1)
            subset.pop()

if __name__ == "__main__" :
    nums = [1,2,3]
    print(Solution().subsets(nums))