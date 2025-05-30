# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        # print(root.val,"<>",p.val,"<>",q.val)

        if root.val == p.val or root.val == q.val: 
            # print("root is same as p or q ",root.val)
            return root

        if (p.val < root.val < q.val) or (p.val > root.val > q.val): 
            # print("p and q are on either side of root ",root.val)
            return root

        if p.val > root.val and q.val > root.val:
            # print("p and q are greater than root ",root.val)
            return self.lowestCommonAncestor(root.right,p,q)

        if p.val < root.val and q.val < root.val: 
            # print("p and q are less than root ",root.val)
            return self.lowestCommonAncestor(root.left,p,q)

        return root