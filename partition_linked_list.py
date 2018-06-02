def partition(head,target):
    
    l1 =None
    l2 =None
    point1 = None
    point2 = None
    answer = None
    if not head:
        return
    while head:
        if head.val < target:
            if not l1:
                l1 = ListNode(head.val)
                point1 = l1
            else:
                l1.next = ListNode(head.val)
                l1 = l1.next
        else:
            if not l2:
                l2 = ListNode(head.val)
                point2 = l2
            else:
                l2.next = ListNode(head.val)
                l2 = l2.next
        head = head.next
            
    
    
    if not point1:
        return point2
    else:
        answer = point1
        while point1.next:
            
            point1 = point1.next
        point1.next = point2
    
    return answer