# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def inorder(self, root,traversed_nodes):
        if root == None:
            return
        
        self.inorder(root.left,traversed_nodes)
        traversed_nodes.append(root.val)
        self.inorder(root.right, traversed_nodes)

    def isValidBST(self, root):    
        if root == None :
            return True
        
        traversed_nodes = []
        self.inorder(root,traversed_nodes)

        if len(traversed_nodes) == 1:
            return True
        elif len(traversed_nodes) == 2:
            return traversed_nodes[0] < traversed_nodes[1]
        else:
            prev_ptr = 0
            curr_ptr = 1 
            next_ptr = 2

            while next_ptr < len(traversed_nodes):

                if ((traversed_nodes[prev_ptr] > traversed_nodes[curr_ptr]) or
                    (traversed_nodes[next_ptr] < traversed_nodes[curr_ptr])) :
                    return False
                prev_ptr += 1
                curr_ptr += 1
                next_ptr += 1
        
        return True
    
        