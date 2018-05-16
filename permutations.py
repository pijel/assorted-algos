class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return permute(nums)
        
def permute(nums):
    if len(nums) == 1:
        return [nums]
    else:
        answer = []
        last_value = nums.pop()
        previous = permute(nums)
        for k in previous:
            for j in range(len(k)+1):
                if k[:j] + [last_value] + k[j:] not in answer:
                    answer.append( k[:j] + [last_value] + k[j:])
        return answer