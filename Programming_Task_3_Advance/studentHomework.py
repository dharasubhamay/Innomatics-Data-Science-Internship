# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        for i in range(len(startTime)):
            if(queryTime in range(startTime[i], endTime[i]+1)):
                cnt += 1
        return cnt
    
if __name__ == "__main__":
    startTime = [1,2,3] 
    endTime = [3,2,7]
    queryTime = 4
    print(Solution().busyStudent(startTime, endTime, queryTime))