"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        s_map = {}
        for ele in s:
            if ele in s_map:
                s_map[ele] += 1
            else:
                s_map[ele] = 1

        for ele in t:
            if ele in s_map:
                if s_map[ele] == 1:
                    del s_map[ele]
                else:
                    s_map[ele] -= 1
            else:
                return False
        
        if len(s_map) == 0:
            return True
        
        return False
                