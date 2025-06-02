from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        
        if root == None: return []

        node_vals = []
        level_node_vals = []
        node_stack = deque()
        node_stack.append(root)
        node_stack.append(None)
        
        while len(node_stack) != 0:
            # print(node_stack)
            curr = node_stack.popleft()
            # print(node_stack)

            if curr == None:
                node_vals.append(level_node_vals)
                # print(level_node_vals,"<><>",node_vals)
                level_node_vals = []
                if len(node_stack) > 0:
                    node_stack.append(None)
            else:
                level_node_vals.append(curr.val)
                if curr.left != None: node_stack.append(curr.left)
                if curr.right != None: node_stack.append(curr.right)
        
        return node_vals