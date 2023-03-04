# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxno = nums[0]
        maxid = 0
        for (idx, num) in enumerate(nums):
            if num > maxno:
                maxno = num
                maxid = idx
        nums[maxid] = 0
        secondmax = nums[0]
        for i in nums:
            if i > secondmax:
                secondmax = i
        result = (maxno - 1) * (secondmax - 1)
        return result

if __name__ == "__main__":
    nums = [3,4,5,2]
    print(Solution().maxProduct(nums))