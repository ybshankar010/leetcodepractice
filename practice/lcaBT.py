# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if root.val == p.val or root.val == q.val: return root

        if (((root.left and root.left == p.val) and 
            (root.right and root.right == q.val)) or
            ((root.left and root.left == q.val) and 
             (root.right and root.right == p.val))):
            return root
        
        