class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """     

        ans = 0
        while n > 1:
            h = getsmallestfactor(n)
            ans += h
            n = n//h
        return ans
    

        
def getsmallestfactor(n):
    i = 2
    while i * i <= n:
        if n %i == 0:
            return i
        i+=1
    return n