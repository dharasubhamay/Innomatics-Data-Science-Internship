# https://leetcode.com/problems/hamming-distance/

from typing import List
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binx = str(bin(x))
        biny = str(bin(y))
        binx = binx[2: len(binx)]
        biny = biny[2: len(biny)]
        maxlen = max(len(binx), len(biny))
        if maxlen == len(binx):
            remlen = maxlen - len(biny)
            zeros = ''
            for i in range(remlen):
                zeros += '0'
            biny = zeros + biny
        elif maxlen == len(biny):
            remlen = maxlen - len(binx)
            zeros = ''
            for i in range(remlen):
                zeros += '0'
            binx = zeros + binx
        cnt = 0
        for (idx, n) in enumerate(binx):
            if n != biny[idx]:
                cnt += 1
        return cnt
    
if __name__ == "__main__" :
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))