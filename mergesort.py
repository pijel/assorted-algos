def mergesort(a):
    
    if len(a) > 1:
        middle = len(a) // 2
        left = a[:middle]
        right = a[middle:]
        
        mergesort(left)
        mergesort(right)
        # by using recursive calls here, we are saying that the left part of a and the right part of a have been sorted in place
        # now we have to use the merge command, being careful that it's saved into a itself
        
        left_index = 0 
        right_index = 0
        a_index = 0
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                a[a_index] = left[left_index]
                left_index += 1
                a_index +=1
                
            else:
                a[a_index] = right[right_index]
                right_index += 1
                a_index +=1
        #now, at least one array has been completely looked through. we'll have to pick up the other one
        
        while left_index < len(left):
            a[a_index] = left[left_index]
            a_index +=1
            left_index +=1
            
        while right_index < len(right):
            a[a_index] = right[right_index]
            a_index +=1
            right_index +=1
        
        