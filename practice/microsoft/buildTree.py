from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.inorder_dict = {}

    def split_at_root(self, val,start_idx,end_idx):

        root_idx = self.inorder_dict.get(val, -1)
        # new_start_idx = start_idx
        # while new_start_idx <= end_idx:
        #     if inorder[new_start_idx] == val:
        #         root_idx = new_start_idx
        #         break
        #     new_start_idx = new_start_idx + 1
        
        # print(val,"::",root_idx)
        
        lt_start, lt_end = start_idx,root_idx-1
        rt_start, rt_end = root_idx+1,end_idx

        return lt_start,lt_end,rt_start,rt_end

    def buildSubTree(self,preorder,inorder,start,end):

        if start > end or not preorder:
            return None
        
        current_node = TreeNode(preorder.popleft())
        print("Creating subtree for the node :: ",current_node.val,"::",start,"::",end)
        if start != end:
            left_subtree_start,left_subtree_end, right_subtree_start, right_subtree_end = self.split_at_root(current_node.val,start,end)

            # print("Left Sub-tree :: ",left_subtree_start," :: ",left_subtree_end)
            # print("Right Sub-tree :: ",right_subtree_start," :: ",right_subtree_end)
            
            current_node.left = self.buildSubTree(preorder,inorder,left_subtree_start,left_subtree_end)
            current_node.right = self.buildSubTree(preorder,inorder,right_subtree_start,right_subtree_end)

        return current_node

    def buildTree(self, preorder, inorder):

        self.inorder_dict = {}
        self.inorder_dict = {inorder[i]:i for i in range(len(inorder))}

        preorder = deque(preorder)
        root = TreeNode(preorder.popleft())

        left_subtree_start,left_subtree_end, right_subtree_start, right_subtree_end = self.split_at_root(root.val,0,len(inorder)-1)

        # print("Left Sub-tree :: ",left_subtree_start," :: ",left_subtree_end)
        # print("Right Sub-tree :: ",right_subtree_start," :: ",right_subtree_end)

        root.left = self.buildSubTree(preorder,inorder,left_subtree_start,left_subtree_end)
        root.right = self.buildSubTree(preorder,inorder,right_subtree_start,right_subtree_end)

        return root
        