class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return solution(matrix)
       
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def add(self,value):
        new_node = DoubleListNode(value)
        if self.first == None and self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.last
            self.last.prev = new_node
            # if we wanted to used single linked lists, this would just be a second linked list pointing in the opposite direction. I think this is better
            self.last = new_node
    def remove(self):
        if not self.first:
            return False
        return_value = self.first.val
        self.first = self.first.prev
        return return_value
    def show(self):
        a = self.first
        while a:
            print (a.val)
            a = a.prev
    def nonempty(self):
        return (self.first != None and self.last != None)     
    def peek(self):
        return self.first.val
        
def getneighbors(matrix,i,j):
    # i is the row
    # j is the column
    
    neighbors = []
    if i != 0:
        neighbors.append([i-1,j])
    if i!= len(matrix) - 1:
        neighbors.append([i+1,j])
    if j!=0:
        neighbors.append([i,j-1])
    if j!=len(matrix[0])-1:
        neighbors.append([i,j+1])
    return neighbors

def getdistance(matrix,i,j):
    
    if matrix[i][j] == 0:
        return 0
    
    q = Queue()
    neighbors = getneighbors(matrix,i,j)
    for k in neighbors:
        q.add([k,1])
    found_zero = False
    while not found_zero:
        current = q.peek()
        if matrix[current[0][0]][current[0][1]] == 0:
            return current[1]
        else:
            new_neighbors = getneighbors(matrix,current[0][0],current[0][1])
            for k in new_neighbors:
                q.add([k, current[1]+1])
        q.remove()
                
def solution(matrix):
    answer = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            answer[i][j] = getdistance(matrix,i,j)
    return answer

class DoubleListNode:
    def __init__(self,x):
        self.val = x
        self.prev = None
        self.next = None