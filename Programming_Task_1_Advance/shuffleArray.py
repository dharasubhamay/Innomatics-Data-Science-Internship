#https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[n+i])
    return result

nums = [2,5,1,3,4,7]
n = 3
res = shuffle(nums, n)
print(res)