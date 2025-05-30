# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None : return list2
        if list2 == None : return list1

        mergedlist = next_ptr = None

        while list1 != None and list2 != None:

            if list1.val > list2.val:
                curr = list2
                list2= list2.next
            else:
                curr = list1
                list1 = list1.next
            
            if mergedlist == None:
                mergedlist = next_ptr = curr
            else:
                next_ptr.next = curr
                next_ptr = next_ptr.next
        
        while list1 != None:
            curr = list1
            list1 = list1.next
            next_ptr.next = curr
            next_ptr = next_ptr.next
        
        while list2 != None:
            curr = list2
            list2 = list2.next
            next_ptr.next = curr
            next_ptr = next_ptr.next
        
        return mergedlist
