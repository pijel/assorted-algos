# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return mergelists(l1,l2)
        
        
def mergelists(l1,l2):
    
    if not l1 and not l2:
        return None
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.val < l2.val:
        new_list = ListNode(l1.val)
        l1 = l1.next
    else:
        new_list = ListNode(l2.val)
        l2 = l2.next
    answer = new_list
    while l1 and l2:
        if l1.val < l2.val:
            new_list.next = ListNode(l1.val)
            new_list = new_list.next
            l1 = l1.next
        else:
            new_list.next = ListNode(l2.val)
            new_list = new_list.next
            l2 = l2.next
    while l1:
        new_list.next = ListNode(l1.val)
        new_list = new_list.next
        l1 = l1.next
    while l2:
        new_list.next = ListNode(l2.val)
        new_list = new_list.next
        l2 = l2.next
      
    return answer