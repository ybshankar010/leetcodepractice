# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_path(self,root,ptr,path=[]):
        
        if root == ptr :
            path.append(root)
            return True
        
        path.append(root)

        path_available = False
        if root.left:
            path_available = self.find_path(root.left,ptr,path)
            if not path_available:
                path.pop()
        
        if not path_available and root.right:
            path_available = self.find_path(root.right,ptr,path)
            if not path_available:
                path.pop()
        
        return path_available


    def lowestCommonAncestor(self, root, p, q):

        if root == p or root == q : return root

        p_path = []
        self.find_path(root,p,p_path)
        q_path = []
        self.find_path(root,q,q_path)

        p_path_set = set(p_path)

        lca = root
        for q_ptr in q_path:
            if q_ptr in p_path_set:
                lca = q_ptr

        return lca
        
        