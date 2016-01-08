# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

"""

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r_list = []
        if root is None:
            return r_list
            
        node_stack = [root.right, root, root.left]
        label_stack = [False, True, False]
        while len(node_stack)>=1:
            node = node_stack.pop()
            label = label_stack.pop()
            if node is None:
                continue
            
            if label:
                r_list.append(node.val)
            else:
                node_stack.append(node.right)
                node_stack.append(node)
                node_stack.append(node.left)
                label_stack.append(False)
                label_stack.append(True)
                label_stack.append(False)
        return r_list
            
            