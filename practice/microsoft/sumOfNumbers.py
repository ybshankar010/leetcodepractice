# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        if l1 == None : return l2
        if l2 == None : return l1

        carry = 0
        
        # 20 = (20//10),(20%10)
        sum_of_numbers = next_ptr = None
        while l1 != None or l2 != None:
            sum_total = l1.val + l2.val + carry
            sum_val = sum_total // 10
            carry = sum_total%10

            curr = ListNode(sum_val,None)
            if sum_of_numbers == None:
                sum_of_numbers = next_ptr = curr
            else:
                next_ptr.next = curr
                next_ptr = next_ptr.next
            
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            sum_total = l1.val + carry
            sum_val = sum_total // 10
            carry = sum_total%10

            curr = ListNode(sum_val,None)
            next_ptr.next = curr
            next_ptr = next_ptr.next

            l1 = l1.next
        
        while l2 != None:
            sum_total = l1.val + carry
            sum_val = sum_total // 10
            carry = sum_total%10

            curr = ListNode(sum_val,None)
            next_ptr.next = curr
            next_ptr = next_ptr.next

            l2 = l2.next
        
        if carry != 0:
            curr = ListNode(carry,None)
            next_ptr.next = curr
        
        return sum_of_numbers

