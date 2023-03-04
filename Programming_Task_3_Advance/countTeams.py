# https://leetcode.com/problems/count-number-of-teams/

from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        arr1, arr2 = [0] * n, [0] * n
        result = 0
        for i, r in enumerate(rating):
            for j in range(i):
                if r > rating[j]:
                    arr1[i] += 1
                    result += arr1[j]
                elif r < rating[j]:
                    arr2[i] += 1
                    result += arr2[j]
        return result

if __name__ == "__main__":
    rating = [2,5,3,4,1]
    print(Solution().numTeams(rating))