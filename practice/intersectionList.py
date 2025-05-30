# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        headASet = set()
        while headA != None:
            headASet.add(headA)
            headA = headA.next
        
        while headB != None:
            if headB in headASet :
                return headB
            headB = headB.next
        
        return None
            