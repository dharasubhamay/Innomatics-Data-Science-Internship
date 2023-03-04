# https://leetcode.com/problems/single-number-ii/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            lst = list(dic.keys())
            if(i in lst):
                dic[i] += 1
            else :
                dic[i] = 1
        for i in dic.keys():
            if dic[i] == 1:
                return i

if __name__ == "__main__":
    nums = [2,2,3,2]
    print(Solution().singleNumber(nums))