# https://leetcode.com/problems/single-number-iii/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for i in nums:
            if(i in s):
                s.remove(i)
            else:
                s.add(i)
        result = list(s)
        return result

if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    print(Solution().singleNumber(nums))