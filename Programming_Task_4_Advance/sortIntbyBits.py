# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ones_arr = []
        for i, n in enumerate(arr):
            res = n // 2
            rem = n % 2
            ones = rem
            while res != 0:
                rem = res % 2
                res = res // 2
                ones += rem
            ones_arr.append(ones)
        result = []
        for i in sorted(zip(ones_arr, arr)):
            result.append(i[1])
        return result

if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8]
    print(Solution().sortByBits(arr))