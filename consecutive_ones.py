class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return maxrun(nums)

def maxrun(nums):
    
    max_run = 0
    current_run = 0
    for i in nums:
        if i==1:
            current_run += 1
            if current_run > max_run:
                max_run = current_run 
        else:
            current_run = 0
          
    return max_run