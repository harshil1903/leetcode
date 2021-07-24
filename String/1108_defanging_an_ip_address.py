
# 1108. Defanging an IP Address
#
# Source : https://leetcode.com/problems/defanging-an-ip-address/
#
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".



class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")

if __name__ == '__main__':
    s = Solution();
    print(s.defangIPaddr("1.1.1.1"))
    print(s.defangIPaddr("255.100.50.0"))