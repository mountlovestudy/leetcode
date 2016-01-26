#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path, q_path = self.getPath(root, p, q)
        ancestor = None
        while True:
            if len(p_path)==0 or len(q_path)==0:
                break
            node_level_p = p_path[-1]
            node_level_q = q_path[-1]
            if node_level_p.node == node_level_q.node:
                ancestor = node_level_p.node
                break
            else:
                if node_level_p.level < node_level_q.level:
                    q_path.pop()
                elif node_level_p.level > node_level_q.level:
                    p_path.pop()
                else:
                    p_path.pop()
                    q_path.pop()
        return ancestor
        
    def getPath(self, root, p, q):
        path_stack = list([])
        path_stack.append(nodeLevel(root, 0, False))
        p_path = []
        q_path = []
        p_label = False
        q_label = False
        while True:
            if len(path_stack) == 0:
                break
            now = path_stack.pop()
            if now.node == p and now.isUnfold:
                p_path = path_stack[:]
                p_path.append(now)
                p_label = True
            if now.node == q and now.isUnfold:
                q_path = path_stack[:]
                q_path.append(now)
                q_label =True
            if p_label and q_label:
                break
            if now.isUnfold or now.node is None :
                continue
            else:
                path_stack.append(nodeLevel(now.node, now.level, True))
                path_stack.append(nodeLevel(now.node.right, now.level+1, False))
                path_stack.append(nodeLevel(now.node.left, now.level+1, False))
        return p_path, q_path
    
class nodeLevel(object):
    def __init__(self, node, level, isUnfold):
        self.node = node
        self.level = level
        self.isUnfold = isUnfold

class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        node = root
        node_level = 0
        p_path = []
        p_path_level = []
        q_path = []
        q_path_level = []
        root_list = []
        root_level = []
        p_label = False
        q_label = False
        to_iter_list = []
        to_iter_level = []
        while True:
            while len(root_list)>0 and root_level[-1] >= node_level:
                root_list.pop()
                root_level.pop()
            if node == p:
                p_label = True
                p_path = root_list[:]
                p_path_level = root_level[:]
                while len(p_path)>0 and p_path_level[-1] >= node_level:
                    p_path.pop()
                    p_path_level.pop()
                p_path.append(node)
            if node == q:
                q_label = True
                q_path = root_list[:]
                q_path_level = root_level[:]
                while len(q_path)>0 and q_path_level[-1] >= node_level:
                    q_path.pop()
                    q_path_level.pop()
                q_path.append(node)
            if p_label and q_label:
                break

            root_list.append(node)
            root_level.append(node_level)
            if node.left is not None:
                if node.right is not None:
                    to_iter_list.append(node.right)
                    to_iter_level.append(node_level+1)
                node = node.left
                node_level = node_level + 1
            elif node.left is None and node.right is not None:
                node = node.right
                node_level = node_level + 1
            elif node.left is None and node.right is None:
                node = to_iter_list.pop()
                node_level = to_iter_level.pop()

        while len(q_path)>0 and len(p_path)>0:
            if len(q_path) > len(p_path):
                q_path.pop()
            elif len(q_path) < len(p_path):
                p_path.pop()
            else:
                if q_path[-1] == p_path[-1]:
                    return q_path[-1]
                else:
                    q_path.pop()
                    p_path.pop()
        return None

if __name__ == "__main__":
    node_left = TreeNode(1)
    node_root = TreeNode(2)
    node_root.left = node_left
    p = node_root
    q = node_left
    Solution().lowestCommonAncestor(node_root, p, q)
