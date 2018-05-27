class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return generate(n)
        
        
        
        
def generate(n): 
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
   
    
    answer = []
    for i in range(1,n):
        comp1 = generate(i)
        comp2 = generate(n-i - 1)
        for k in comp1:
            for j in comp2:
                answer.append("("+k+")"+j)
                answer.append (k + "(" + j + ")")
                
    return list(set(answer))
