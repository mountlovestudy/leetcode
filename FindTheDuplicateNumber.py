"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_nums = 1
        max_nums = len(nums)-1
        mid_nums = (min_nums + max_nums) / 2
        while mid_nums < max_nums:
            num = 0
            for i in nums:
                if i <= mid_nums and i >= min_nums:
                    num += 1
            if num > (mid_nums-min_nums+1):
                max_nums = mid_nums
            else:
                min_nums = mid_nums+1
            mid_nums = (min_nums + max_nums) / 2
        return max_nums
            
class Solution1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gap_2_v = nums[nums[0]] 
        gap_1_v = nums[0]

        while gap_1_v != gap_2_v:
            gap_1_v = nums[gap_1_v]
            gap_2_v = nums[nums[gap_2_v]]
            
        gap_2_v = nums[0]
        gap_1_v = nums[gap_1_v]
        while gap_1_v != gap_2_v:
            gap_2_v = nums[gap_2_v]
            gap_1_v = nums[gap_1_v]
        return gap_1_v
            