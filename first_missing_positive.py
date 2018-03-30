def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
        
    """
    if not nums:
        return 1
    k = [i for i in range(1,len(nums)+2)]
     m = [i for i in k if i not in nums]
    #print(m)
    return min(m)