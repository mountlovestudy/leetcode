"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
            
        r_list = [root.val]
        root_stack = [root.right, root.left]
        while len(root_stack) >= 1:
            node = root_stack.pop()
            if node is not None:
                r_list.append(node.val)
                root_stack.append(node.right)
                root_stack.append(node.left)
        return r_list
        