#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def findNumbers(nums):
        evencnt = 0
        for num in nums:
            cnt = 0
            while num != 0:
                num = num // 10
                cnt += 1
            if(cnt % 2 == 0):
                evencnt += 1
        return evencnt

nums = [12,345,2,6,7896]
even = findNumbers(nums)
print(even)