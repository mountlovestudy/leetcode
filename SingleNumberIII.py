"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_value = 0
        for num in nums:
            xor_value = xor_value ^ num
            
        posit = 0
        while (xor_value >> posit) != 0 and (xor_value >> posit) % 2 == 0:
            posit += 1
        
        xor_v1 = 0
        xor_v0 = 0
        
        for num in nums:
            if self.isOne(num, posit):
                xor_v1 = xor_v1 ^ num
            else:
                xor_v0 = xor_v0 ^ num
                
        return [xor_v0, xor_v1]
            
    def isOne(self, value, posit):
        """
        :type value: int
        :type posit: int
        :rtype: boolean
        """
        return (value >> posit) % 2 != 0