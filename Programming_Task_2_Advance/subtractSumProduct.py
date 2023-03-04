# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def subtractProductAndSum(n):
        strnum = str(n)
        summ = 0
        product = 1
        for i in strnum:
            summ += int(i)
            product *= int(i)
        result = product - summ
        return result

n = 234
print(subtractProductAndSum(n))