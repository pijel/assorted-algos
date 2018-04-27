# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return reverse(to_list(to_number(l1) + to_number(l2)))
        
def to_number(head):
    number = 0
    head = reverse(head)
    while head:
        number = 10 * number + head.val
        head = head.next
    return number

def to_list(num):
    head = ListNode(None)
    start = head
    if num == 0:
        start.val = 0
        return start 
    
    while num > 0:
        head.val = num %10
        num = num //10
        nex = ListNode(None)
        head.next = nex
        head = nex 
    return reverse(start).next
        
def reverse(head):
    
    answer = None
    
    while head:
        next_node = head.next
        head.next = answer
        answer = head
        head = next_node
        
        
        
    return answer
                