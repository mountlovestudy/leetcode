"""
Reverse a singly linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        bef_node = head
        node = bef_node.next
        bef_node.next = None
        while node is not None:
            node_next = node.next
            node.next = bef_node
            bef_node = node
            node = node_next
        return bef_node