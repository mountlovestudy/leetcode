"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele_dict = {}
        n = len(nums)
        r_ele = None
        for ele in nums:
            if ele in ele_dict:
                ele_dict[ele] += 1
            else:
                ele_dict[ele] = 1
            if ele_dict[ele] > n/2:
                r_ele = ele
                break
        return r_ele

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        r_value = 0
        for ele in nums:
            if num == 0:
                r_value = ele
                num += 1
            else:
                if ele == r_value:
                    num += 1
                else:
                    num -= 1
        return r_value