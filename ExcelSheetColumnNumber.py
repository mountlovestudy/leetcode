"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        s_len = len(s)
        
        for i in range(len(s)):
            bit_val = ord(s[s_len-i-1]) - 64
            val += 26 ** i * bit_val
        
        return val