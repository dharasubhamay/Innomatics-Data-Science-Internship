# https://leetcode.com/problems/counting-bits/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            binnum = str(bin(i))
            cnt1 = 0
            for j in binnum:
                if j == '1':
                    cnt1 += 1
            result.append(cnt1)
        return result

if __name__ == "__main__":
    n = 5
    print(Solution().countBits(n))