"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

"""

class Solution_V1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        value = 0 
        while num != 0:
	        remainder = num % 10
	        num = num / 10
	        value = (value + remainder) / 10 + (value + remainder) % 10

	    return value


"""
	Reference https://en.wikipedia.org/wiki/Digital_root
"""
class Solution_V2(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num % 9 if num % 9 !=0 else 9) if num != 0 else 0