# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        1.Traverse through both the list simetaneously
        2.Computer the sum at each pos
            2.1 Mod for current pos digit
            3.1 Division for carry 
        3.If both the list exhausts then calculation completed
        T.C : O(N)
        S.C : O(max(len(l1),len(l2)))+1
        """
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while (l1 != None or l2 != None or carry != 0):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + carry
            carry = sum // 10
            new_node = ListNode(sum % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next 

    
