def reverse(head):
    
    answer = None
    
    while head:
        next_node = head.next
        head.next = answer
        answer = head
        head = next_node
        
        
        
    return answer
        
    
#build list before m, from m to n, after n 

def reversebetween(head,m,n):
    
    l1 = None
    point1 = None
    
    i = 1
    
    while i < m:
        if not l1:
            l1 = ListNode(head.val)
            point1 = l1
        else:
            l1.next = ListNode(head.val)
            l1 = l1.next
        head = head.next
        i +=1
        
    l2 = None
    point2 = None
    while i >= m and i <= n:
        if not l2:
            l2 = ListNode(head.val)
            point2 = l2
            
        else:
            l2.next = ListNode(head.val)
            l2 = l2.next
        head = head.next
        i+=1
        
    point2 = reverse(point2)
    
    l3 = None
    point3 =  None
    while head:
        if not l3:
            l3 = ListNode(head.val)
            point3 = l3
        else:
            l3.next = ListNode(head.val)
            l3 = l3.next
        head = head.next
        i +=1
        
        
    answer = point1
    if point1:
        while point1.next:
            point1 = point1.next
        point1.next = point2
    else:
        answer = point2
    while point2.next:
        point2 = point2.next
    point2.next = point3
    
    return answer