#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

n = int(input().strip())
if(n%2 != 0):
    print("Weird")
else:
    if(n >= 2 and n <= 5):
        print("Not Weird")
    if(n >= 6 and n <= 20):
        print("Weird")
    if(n > 20):
        print("Not Weird")