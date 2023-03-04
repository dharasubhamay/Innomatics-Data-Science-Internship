#https://leetcode.com/problems/defanging-an-ip-address/

def defangIPaddr(address):
        new_string = address.replace('.', '[.]')
        return new_string

ip = input()
res = defangIPaddr(ip)
print(res)