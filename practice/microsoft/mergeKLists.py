# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self,l1,l2):
        if l1 == None: return l2
        if l2 == None: return l1

        merged_list = next_ptr = None
        while l1 != None and l2 != None:

            if l1.val < l2.val :
                curr = l1
                l1 = l1.next
            else:
                curr = l2
                l2 = l2.next
            
            if merged_list == None:
                merged_list = curr
                next_ptr = merged_list
            else:
                next_ptr.next = curr
                next_ptr = next_ptr.next
        
        if l1 :
            next_ptr.next = l1
        else:
            next_ptr.next = l2

        return merged_list

    def mergeKLists(self, lists):
        if len(lists) <= 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        merged_list = None
        for l in lists:
            merged_list = self.mergeTwoLists(merged_list,l)
        
        return merged_list
    

# if __name__ == "__main__":
#     lists = [None,None, None]
#     print(any(lists))