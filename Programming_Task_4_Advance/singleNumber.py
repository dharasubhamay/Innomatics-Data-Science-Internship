# https://leetcode.com/problems/single-number/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_num = 0
        for i in nums:
            xor_num ^= i
        return xor_num

if __name__ == "__main__":
    nums = [2,2,1]
    print(Solution().singleNumber(nums))