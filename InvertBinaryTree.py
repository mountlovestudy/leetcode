"""
Invert a binary tree.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        node_tmp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(node_tmp)
        
        return root