# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        return remove_node(head,n)
    
def get_list_len(head):
    
    if not head:
        return 0
    length = 1
    
    while head.next:
        length += 1
        head = head.next
    return length

def remove_node(head,n):
    size = get_list_len(head)
    
    if size == n:
        return head.next
    node_to_remove = size - n
    
    
    start = head
    position = 1
    
    while head:
        if position == node_to_remove:
            head.next = head.next.next
        head = head.next
        position +=1
    return start