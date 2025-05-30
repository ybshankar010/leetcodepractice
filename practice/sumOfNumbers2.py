# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseList(self,l):
        if l == None:
            return l
        
        nodes = []
        while l != None:
            nodes.append(l)
            l = l.next
        
        reversed_l=next_ptr = None
        while len(nodes)>0:
            curr = nodes.pop() 
            if reversed_l == None:
                reversed_l = next_ptr = curr
            else:
                next_ptr.next = curr
                next_ptr = next_ptr.next
        
        next_ptr.next = None

        return reversed_l


    def addNumbers(self,l1,l2):
        final_sum = next_ptr = None

        carry = 0
        while l1 != None and l2 != None:
            total = l1.val + l2.val + carry
            sum_val = total%10
            carry = total // 10

            curr = ListNode(sum_val,None)
            if final_sum == None:
                final_sum = next_ptr = curr
            else:
                next_ptr.next = curr
                next_ptr= next_ptr.next
            
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            total = l1.val + carry
            sum_val = total%10
            carry = total // 10

            curr = ListNode(sum_val,None)
            next_ptr.next = curr
            next_ptr = next_ptr.next
            l1 = l1.next
        
        while l2 != None:
            total = l2.val + carry
            sum_val = total%10
            carry = total // 10

            curr = ListNode(sum_val,None)
            next_ptr.next = curr
            next_ptr = next_ptr.next
            l2 = l2.next
        
        if carry > 0:
            curr = ListNode(carry, None)
            next_ptr.next = curr
        
        return final_sum


    def addTwoNumbers(self, l1, l2):
        
        if l1 == None : return l1
        if l2 == None : return l2

        temp_l1 = self.reverseList(l1)
        temp_l2 = self.reverseList(l2)

        sum_of_nums = self.addNumbers(temp_l1,temp_l2)

        final_sum = self.reverseList(sum_of_nums)

        return final_sum
        