# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sort_me = to_array(head)
        sort_me.sort()
        return to_list(sort_me)
        
        
        
def to_array(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
        
    return out

def to_list(array):
    
    if not array:
        return None
    node = ListNode(array[-1])
    if len(array) == 1:
        return node
    else:
        for i in range(len(array)-2,-1,-1):
            old_node = node
            node = ListNode(array[i])
            node.next = old_node
    return node
    
    