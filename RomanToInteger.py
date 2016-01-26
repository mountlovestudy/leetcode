"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I':1, 'V':5, 'X':10, 'C':100, 'L':50, 'D':500, 'M':1000}
        if len(s) == 1:
            return roman_dict[s]
        rint = 0
        for i in range(1, len(s), 1):
            if roman_dict[s[i]] > roman_dict[s[i-1]]:
                rint += -roman_dict[s[i-1]]
            else:
                rint += roman_dict[s[i-1]]
        rint += roman_dict[s[-1]]
        return rint