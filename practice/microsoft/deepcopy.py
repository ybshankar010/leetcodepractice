"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if head == None : return None
        head_next_ptr = head
        deep_copy_ptr = deep_copy_next_ptr = None

        node_dict = {}
        while head_next_ptr != None:
            curr = Node(head_next_ptr.val,None)
            if deep_copy_next_ptr == None:
                deep_copy_ptr = deep_copy_next_ptr = curr
            else:
                deep_copy_next_ptr.next = curr
                deep_copy_next_ptr = deep_copy_next_ptr.next
            
            node_dict[head_next_ptr] = curr
            head_next_ptr = head_next_ptr.next
        
        for old_node, new_node in node_dict.items():
            old_random_node = old_node.random
            print(old_random_node)
            if old_random_node == None:
                continue

            new_random_node = node_dict[old_random_node]
            new_node.random = new_random_node

        print("===",deep_copy_ptr)
        return deep_copy_ptr