# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

from typing import List

class Solution:
    def numberOfSteps(self, num: int) -> int:
        stepcnt = 0
        while(num != 0):
            if(num % 2 == 0):
                num /= 2
                stepcnt += 1
            else:
                num -= 1
                stepcnt += 1
        return stepcnt

if __name__ == "__main__":
    num = 14
    print(Solution().numberOfSteps(num))