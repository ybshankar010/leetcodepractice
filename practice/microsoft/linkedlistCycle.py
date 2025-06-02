# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        
        first = head
        second = head.next.next

        while first != None and second != None:
            if first == second:
                return True
            first = first.next
            second = second.next
            if second != None:
                second = second.next

        return False