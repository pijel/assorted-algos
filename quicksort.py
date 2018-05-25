def quicksort(a):
    # pick a partition element
    # put all the elements less than it to the left
    # put all the elements more than it to the right
    if len(a) > 1:
        pivot = a[-1]
        left = [x for x in a if x < pivot]
        pivots = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        return quicksort(left) + pivots + quicksort(right)
    return a
        