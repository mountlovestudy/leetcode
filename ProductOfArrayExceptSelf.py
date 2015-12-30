"""

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if [] == nums:
            return nums
        if len(nums) == 1:
            return [1]
            
        result_list = [1]
        product_val = nums[0]
        for i in range(1, len(nums), 1):
            result_list.append(product_val)
            product_val *= nums[i]
        
        product_val = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            result_list[i] *= product_val
            product_val *= nums[i]
        
        return result_list