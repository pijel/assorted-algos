class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix = zeroexpansion([i,j],matrix)
                
        matrix = remove_a(matrix)
                    
        
        
def zeroexpansion(coord,matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == coord[1]:
                if matrix[i][j]!=0:
                    matrix[i][j] = 'a'
    for i in range(len(matrix[coord[0]])):
        if matrix[coord[0]][i]!=0:
            matrix[coord[0]][i] = 'a'
    return matrix 
        
def remove_a(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'a':
                matrix[i][j] = 0
    return matrix