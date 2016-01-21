"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
"""

class Solution1(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_product = 0
        for i in range(len(words)):
        	word = words[i]
        	word_len = len(word)
        	for j in range(i, len(words), 1):
        		compare_word = words[j]
        		if word_len * len(compare_word) <= max_product:
        			continue
        		if self.isIn(word, compare_word):
        			continue
        		max_product = word_len * len(compare_word)
        return max_product

    def isIn(serlf, worda, wordb):
    	for ele in worda:
    		if ele in wordb:
    			return True
    	return False

class Solution2(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_product = 0
        bit_word = {}
        for word in words:
            k = 0
            for w in set(word):
            	k += 1 << (ord(w) - ord('a'))
            for compare_word, v in bit_word.items():
                if k & v == 0:
                    max_product = max(max_product, len(word) * len(compare_word))
            bit_word[word] = k
        return max_product

print Solution2().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
