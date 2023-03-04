#https://leetcode.com/problems/xor-operation-in-an-array/

def xorOperation(n, start):
    arr = []
    for i in range(n):
        arr.append(start + 2 * i)
    xor_res = 0
    for i in arr:
        xor_res = xor_res ^ i
    return xor_res

n = 5
start = 0
print(xorOperation(n, start))