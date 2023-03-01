#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kidsWithCandies(candies, extraCandies):
    result = []
    greatestCandy = max(candies)
    for i in candies:
        if((i+extraCandies) >= greatestCandy):
            result.append(True)
        else:
            result.append(False)
    return result

candies = [2,3,5,1,3]
extraCandies = 3
res = kidsWithCandies(candies, extraCandies)
print(res)